import os
import logging

from config import LOG_FOLDER

# --------------------------------------------------
# Create Log Folder
# --------------------------------------------------

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(LOG_FOLDER, "pipeline.log")

# --------------------------------------------------
# Logger Configuration
# --------------------------------------------------

logger = logging.getLogger("AdventureWorksPipeline")

# Prevent duplicate logs
if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler
    file_handler = logging.FileHandler(
        LOG_FILE,
        mode="a",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)