"""
brain/command_parser.py

Parses execution plans into clean,
structured commands.
"""


class CommandParser:

    def parse(self, plan: dict) -> dict:

        task = plan["task"]

        if task == "OPEN_APPLICATION":

            app = plan["arguments"]["application"]

            app = (
                app.lower()
                .replace("open", "")
                .replace("launch", "")
                .replace("start", "")
                .replace("run", "")
                .strip()
            )

            plan["arguments"]["application"] = app

        return plan