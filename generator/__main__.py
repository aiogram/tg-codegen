import logging
from datetime import datetime

import sys

from generator.cli import main

if __name__ == "__main__":
    created_at = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logging.basicConfig(level=logging.INFO, filename=f"generator-{created_at}.log")
    sys.exit(main(sys.argv))
