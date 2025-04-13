import logging
from pathlib import Path
from datetime import datetime

# Создаем папку для логов, если ее нет
LOG_DIR = Path(__file__).parent.parent / "data" / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Формат логов
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Имя файла с текущей датой
LOG_FILE = LOG_DIR / f"system_{datetime.now().strftime('%Y-%m-%d')}.log"

# Настройка логгера
def setup_logger():
    logger = logging.getLogger("bank_system")
    logger.setLevel(logging.INFO)

    # Форматирование
    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)

    # Обработчик для файла
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Обработчик для консоли (по желанию)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Добавляем обработчики
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)  # Убрать, если не нужен вывод в консоль

    return logger

# Инициализация логгера
logger = setup_logger()