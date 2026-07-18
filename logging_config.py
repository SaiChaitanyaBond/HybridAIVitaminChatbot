"""
Application Logging Configuration

This module configures application-wide logging.
Logs are written to both the console and a log file.
"""

import logging
from pathlib import Path

# ---------------------------------------------------------------------
# Create logs directory if it doesn't exist
# ---------------------------------------------------------------------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------
# Configure root logger
# ---------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(
            LOG_DIR / "hybrid_chatbot.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)

logger.info("Logging initialized successfully.")