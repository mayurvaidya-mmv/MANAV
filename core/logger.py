"""
MANAS Logger

Central logging service.
"""

from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self):

        self.log_dir = Path("logs")

        self.log_dir.mkdir(
            exist_ok=True
        )

        filename = datetime.now().strftime("%Y-%m-%d") + ".log"

        self.log_file = self.log_dir / filename

    def _write(self, level: str, message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        line = f"[{timestamp}] [{level}] {message}"

        print(line)

        with open(

            self.log_file,

            "a",

            encoding="utf-8"

        ) as file:

            file.write(line + "\n")

    def info(self, message: str):

        self._write(

            "INFO",

            message

        )

    def warning(self, message: str):

        self._write(

            "WARNING",

            message

        )

    def error(self, message: str):

        self._write(

            "ERROR",

            message

        )

    def debug(self, message: str):

        self._write(

            "DEBUG",

            message

        )