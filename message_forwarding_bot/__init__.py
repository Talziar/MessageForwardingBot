"""Bot initialization."""

import json
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from sys import stderr, stdout

WORK_DIR = Path(__package__).absolute()
PARENT_DIR = WORK_DIR.parent

# Read bot config
CONFIG = json.loads((PARENT_DIR / "config.json").read_text())
API_KEY = CONFIG["api_key"]
API_HASH = CONFIG["api_hash"]
USERNAME = CONFIG["username"]
USER_ID = CONFIG["tg_user_id"]


# Logging
LOG_FILE = PARENT_DIR / "last_run.log"
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
FORMATTER: logging.Formatter = logging.Formatter(LOG_FORMAT)
handler = TimedRotatingFileHandler(LOG_FILE, when="d", interval=1, backupCount=3)
logging.basicConfig(filename=str(LOG_FILE), filemode="w", format=LOG_FORMAT)
OUT = logging.StreamHandler(stdout)
ERR = logging.StreamHandler(stderr)
OUT.setFormatter(FORMATTER)
ERR.setFormatter(FORMATTER)
OUT.setLevel(logging.INFO)
ERR.setLevel(logging.WARNING)
LOGGER = logging.getLogger()
LOGGER.addHandler(OUT)
LOGGER.addHandler(ERR)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)
