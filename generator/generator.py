import contextlib
import logging
import pathlib
import re
from collections import defaultdict
from functools import reduce
from typing import Any, DefaultDict, Dict, List, Optional, Set

import autoflake
import black
import isort
import jinja2
import yaml

from generator.consts import TELEGRAM_TYPE_PATTERN
from generator.normalizers import limit_length, md_line_breaks, pythonize_name
from generator.specials import EXTRA
from generator.structures import Entity, Group

templates_dir: pathlib.Path = pathlib.Path(__file__).parent / "templates"

log = logging.getLogger(__name__)


class Generator:
    def __init__(self, groups: List[Group]):
        self.groups = groups
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=[templates_dir]))
        self.env.filters.update(
            {
                "pythonize": pythonize_name,
                "class_name": lambda name: name[0].upper() + name[1:],
                "first_line": lambda text: text.split("\n")[0],
                "limit_length": limit_length,
                "md_line_breaks": md_line_breaks,
                "header": lambda value, symbol: symbol * len(value),
            }
        )
        self.env.globals.update({"len": len, "EXTRA": EXTRA})

        self.telegram_types = {
            entity.name for group in groups for entity in group.childs if entity.is_type
        }
        self.telegram_methods = {
            entity.name for group in groups for entity in group.childs if entity.is_method
        }

    def generate(self, out_dir: pathlib.Path):
        log.info("Start generating code")
        for group in self.groups:
            log.info("Visit group %r", group.title)
            for entity in group.childs:
                if entity.is_method:
                    self.generate_method(entity, out_dir)
                else:
                    self.generate_type(entity, out_dir)
            log.info("Leave group %r", group.title)
        with self.open_file(out_dir, "aiogram", "api", "types", "__init__.py") as f:
            f.write(self.render_template("types.py.jinja2", {"groups": self.groups}))
        with self.open_file(out_dir, "aiogram", "api", "methods", "__init__.py") as f:
            f.write(self.render_template("methods.py.jinja2", {"groups": self.groups}))
        with self.open_file(out_dir, "aiogram", "api", "client", "bot.py") as f:
            f.write(self.render_template("bot.py.jinja2", {"groups": self.groups}))

        with self.open_file(out_dir, "docs", "api", "methods", "index.rst") as f:
            f.write(
                self.render_template(
                    "methods_list.md.jinja2", {"groups": self.groups}, reformat_code=False
                )
            )
        with self.open_file(out_dir, "docs", "api", "types", "index.rst") as f:
            f.write(
                self.render_template(
                    "types_list.md.jinja2", {"groups": self.groups}, reformat_code=False
                )
            )

    def _code_autoflake(self, code: str) -> str:
        return autoflake.fix_code(
            code,
            additional_imports=None,
            expand_star_imports=True,
            remove_all_unused_imports=True,
            remove_duplicate_keys=True,
            remove_unused_variables=False,
            ignore_init_module_imports=False,
        )

    def _code_isort(self, code: str) -> str:
        return isort.SortImports(file_contents=code).output

    def _code_black(self, code: str) -> str:
        try:
            return black.format_file_contents(
                code,
                fast=True,
                mode=black.FileMode(target_versions={black.TargetVersion.PY37}, line_length=99),
            )
        except black.NothingChanged:
            return code
        except black.InvalidInput:
            print(code)
            raise

    def render_template(
        self, template_name: str, context: Dict[str, Any], reformat_code: bool = True
    ):
        log.info("Render template %r with context %s", template_name, context)
        code = self.env.get_template(template_name).render(context)

        if reformat_code:
            code = self._code_autoflake(code)
            code = self._code_isort(code)
            code = code.replace("if TYPE_CHECKING:  # pragma: no cover\n    pass\n", "")
            code = self._code_autoflake(code)
            code = self._code_isort(code)
            code = self._code_black(code)

        def fix_line(line: str) -> str:
            if not line.strip():
                line = ""
            return line

        code = "\n".join(map(fix_line, code.split("\n"))).strip() + "\n"
        return code

    def generate_method(self, entity: Entity, out_dir: pathlib.Path):
        log.info("Visit method %r -> %r", entity.name, entity.pythonic_name)
        imports = self.extract_imports(entity, with_returning=True)
        imports["typing"].update({"Dict", "Any"})
        with self.open_entity_file(out_dir / "aiogram", entity) as f:
            code = self.render_template("method.py.jinja2", {"entity": entity, "imports": imports})
            f.write(code)
        with self.open_entity_file(out_dir / "docs", entity, is_doc=True) as f:
            doc = self.render_template(
                "method.md.jinja2", {"entity": entity, "imports": imports}, reformat_code=False
            )
            f.write(doc)
        with self.open_file(
            out_dir / "tests" / "test_api" / "test_methods" / f"test_{entity.pythonic_name}.py"
        ) as f:
            doc = self.render_template("test_method.py.jinja2", {"entity": entity})
            f.write(doc)

    def generate_type(self, entity: Entity, out_dir: pathlib.Path):
        log.info("Visit type %r", entity.name)
        imports = self.extract_imports(entity)
        with self.open_entity_file(out_dir / "aiogram", entity) as f:
            code = self.render_template("type.py.jinja2", {"entity": entity, "imports": imports})
            f.write(code)

        with self.open_entity_file(out_dir / "docs", entity, is_doc=True) as f:
            doc = self.render_template(
                "type.md.jinja2", {"entity": entity, "imports": imports}, reformat_code=False
            )
            f.write(doc)

    def extract_imports(
        self,
        entity: Entity,
        with_returning: bool = False,
        imports: Optional[DefaultDict[str, Set[str]]] = None,
    ):
        if imports is None:
            imports = defaultdict(set)
        imports["typing"].add("TYPE_CHECKING")
        for annotation in entity.annotations:
            # typing
            for from_typing in {"Any", "Union", "Optional", "List"}:
                if from_typing in annotation.python_type:
                    imports["typing"].add(from_typing)
            # Telegram
            for telegram_type in self.telegram_types:
                if telegram_type != entity.name and re.findall(
                    TELEGRAM_TYPE_PATTERN.format(type=telegram_type), annotation.python_type
                ):
                    imports["telegram"].add(telegram_type)

            if "datetime" in annotation.python_type:
                imports["extra"].add("import datetime")
        if entity.extends:
            imports["extra"].add(
                f"from .{pythonize_name(entity.extends[0])} import {entity.extends[0]}"
            )
        if with_returning:
            for from_typing in {"Any", "Union", "Optional", "List"}:
                if from_typing in entity.python_returning_type:
                    imports["typing"].add(from_typing)
            for telegram_type in self.telegram_types:
                if re.findall(
                    TELEGRAM_TYPE_PATTERN.format(type=telegram_type), entity.python_returning_type
                ):
                    imports["telegram"].add(telegram_type)
        imports["telegram"].add("InputFile")
        return imports

    @contextlib.contextmanager
    def open_entity_file(self, out_dir: pathlib.Path, entity: Entity, is_doc: bool = False):
        ext = "rst" if is_doc else "py"
        with self.open_file(
            out_dir, "api", ["types", "methods"][entity.is_method], f"{entity.pythonic_name}.{ext}"
        ) as f:
            yield f

    @contextlib.contextmanager
    def open_file(self, out_dir: pathlib.Path, *path):
        file_path = reduce(pathlib.Path.joinpath, [out_dir, *path])
        log.info("Open file %r", file_path)
        with file_path.open("w") as f:
            yield f
        log.info("Close file %r", file_path)
