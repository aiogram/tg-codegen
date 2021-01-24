import logging

import pypandoc
import sys

from generator.cli import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, stream=sys.stdout)
    sys.exit(main(sys.argv))
