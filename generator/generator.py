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

from generator.consts import TELEGRAM_TYPE_PATTERN
from generator.normalizers import limit_length, pythonize_name
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
            }
        )
        self.env.globals.update(
            {"len": len,}
        )

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
        with self.open_file(out_dir, "api", "types", "__init__.py") as f:
            f.write(self.render_template("types.py.jinja2", {"groups": self.groups}))
        with self.open_file(out_dir, "api", "methods", "__init__.py") as f:
            f.write(self.render_template("methods.py.jinja2", {"groups": self.groups}))
        with self.open_file(out_dir, "api", "client", "bot.py") as f:
            f.write(self.render_template("bot.py.jinja2", {"groups": self.groups}))

    def render_template(self, template_name: str, context: Dict[str, Any]):
        log.info("Render template %r with context %s", template_name, context)
        code = self.env.get_template(template_name).render(context)

        code = autoflake.fix_code(
            code,
            additional_imports=None,
            expand_star_imports=True,
            remove_all_unused_imports=True,
            remove_duplicate_keys=True,
            remove_unused_variables=False,
            ignore_init_module_imports=False,
        )
        code = isort.SortImports(file_contents=code,).output
        try:
            code = black.format_file_contents(
                code,
                fast=True,
                mode=black.FileMode(target_versions={black.TargetVersion.PY37}, line_length=99),
            )
        except black.NothingChanged:
            pass

        return code

    def generate_method(self, entity: Entity, out_dir: pathlib.Path):
        log.info("Visit method %r -> %r", entity.name, entity.pythonic_name)
        imports = self.extract_imports(entity, with_returning=True)
        imports["typing"].update({"Dict", "Any"})
        with self.open_entity_file(out_dir, entity) as f:
            code = self.render_template(
                "method.py.jinja2", {"entity": entity, "imports": imports},
            )
            f.write(code)

    def generate_type(self, entity: Entity, out_dir: pathlib.Path):
        log.info("Visit type %r", entity.name)
        with self.open_entity_file(out_dir, entity) as f:
            code = self.render_template(
                "type.py.jinja2", {"entity": entity, "imports": self.extract_imports(entity)},
            )
            f.write(code)

    def extract_imports(
        self,
        entity: Entity,
        with_returning: bool = False,
        imports: Optional[DefaultDict[str, Set[str]]] = None,
    ):
        if imports is None:
            imports = defaultdict(set)

        for annotation in entity.annotations:
            # typing
            for from_typing in {"Any", "Union", "Optional", "List"}:
                if from_typing in annotation.python_type:
                    imports["typing"].add(from_typing)
            # Telegram
            for telegram_type in self.telegram_types:
                if telegram_type != entity.name and re.findall(
                    TELEGRAM_TYPE_PATTERN.format(type=telegram_type), annotation.python_type,
                ):
                    imports["telegram"].add(telegram_type)
                    imports["typing"].add("TYPE_CHECKING")
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
                    TELEGRAM_TYPE_PATTERN.format(type=telegram_type), entity.python_returning_type,
                ):
                    imports["telegram"].add(telegram_type)
        return imports

    @contextlib.contextmanager
    def open_entity_file(self, out_dir: pathlib.Path, entity: Entity):
        with self.open_file(
            out_dir, "api", ["types", "methods"][entity.is_method], f"{entity.pythonic_name}.py",
        ) as f:
            yield f

    @contextlib.contextmanager
    def open_file(self, out_dir: pathlib.Path, *path):
        file_path = reduce(pathlib.Path.joinpath, [out_dir, *path])
        log.info("Open file %r", file_path)
        with file_path.open("w") as f:
            yield f
        log.info("Close file %r", file_path)
