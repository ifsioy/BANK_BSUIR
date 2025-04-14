import logging
from pathlib import Path
from datetime import datetime

LOG_DIR = Path(__file__).parent.parent / "data" / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_FILE = LOG_DIR / f"system_{datetime.now().strftime('%Y-%m-%d')}.log"

def setup_logger():
    logger = logging.getLogger("bank_system")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)

    file_handler = logging.FileHandler(
        LOG_DIR / f"system_{datetime.now().strftime('%Y-%m-%d')}.log"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

logger = setup_logger()