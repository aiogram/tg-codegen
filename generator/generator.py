import contextlib
import logging
import pathlib
from functools import reduce
from typing import Any, Dict, List

import jinja2

from generator.structures import Entity, Group

templates_dir: pathlib.Path = pathlib.Path(__file__).parent / "templates"

log = logging.getLogger(__name__)


class Generator:
    def __init__(self, groups: List[Group]):
        self.groups = groups
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath=[templates_dir])
        )
        self.telegram_types = {
            entity.name for group in groups for entity in group.childs if entity.is_type
        }
        self.telegram_methods = {
            entity.name
            for group in groups
            for entity in group.childs
            if entity.is_method
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
        with self.open_file(out_dir, "types", "__init__.py") as f:
            f.write(self.render_template("types.py.jinja2", {"groups": self.groups}))

    def render_template(self, template_name: str, context: Dict[str, Any]):
        return self.env.get_template(template_name).render(context)

    def generate_method(self, entity: Entity, out_dir: pathlib.Path):
        log.info("Visit method %r -> %r", entity.name, entity.pythonic_name)

    def generate_type(self, entity: Entity, out_dir: pathlib.Path):
        log.info("Visit type %r", entity.name)
        with self.open_entity_file(out_dir, entity) as f:
            code = self.render_template(
                "type.py.jinja2", {"entity": entity}
            )
            f.write(code)

    @contextlib.contextmanager
    def open_entity_file(self, out_dir: pathlib.Path, entity: Entity):
        with self.open_file(
            out_dir,
            ["types", "methods"][entity.is_method],
            f"{entity.pythonic_name}.py",
        ) as f:
            yield f

    @contextlib.contextmanager
    def open_file(self, out_dir: pathlib.Path, *path):
        file_path = reduce(pathlib.Path.joinpath, [out_dir, *path])
        log.info("Open file %r", file_path)
        with file_path.open("w") as f:
            yield f
        log.info("Close file %r", file_path)
