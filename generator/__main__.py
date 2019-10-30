import logging
import sys

from generator.cli import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main(sys.argv))
