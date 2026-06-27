"""
MANAS Logger
"""

from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self):

        self.log_dir = Path("logs")

        self.log_dir.mkdir(exist_ok=True)

        today = datetime.now().strftime("%Y-%m-%d")

        self.file = self.log_dir / f"{today}.log"

    def log(self, message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(
            self.file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(f"[{timestamp}] {message}\n")