import logging
import pathlib
import sys
import typing

from generator.generator import Generator
from generator.parser import Parser

script_path = pathlib.Path(__file__).parent
out_dir = script_path.parent


def main(argv: typing.List[str]) -> int:
    parser = Parser()

    groups = parser.parse()
    generator = Generator(groups)
    generator.generate(out_dir)

    return 0
