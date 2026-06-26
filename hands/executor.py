"""
hands/executor.py

Executes actions on the local Windows computer.
"""

import os


class Executor:

    def execute(self, plan: dict):
        """
        Execute the generated execution plan.
        """

        task = plan["task"]

        if task == "OPEN_APPLICATION":

            app = plan["arguments"]["application"]

            self.open_application(app)

            return

        print(f"Unknown task: {task}")

    def open_application(self, app: str):
        """
        Opens an application on Windows.
        """

        applications = {
            "chrome": "chrome.exe",
            "google chrome": "chrome.exe",

            "edge": "msedge.exe",

            "calculator": "calc.exe",
            "calc": "calc.exe",

            "notepad": "notepad.exe",

            "paint": "mspaint.exe",

            "powershell": "powershell.exe",

            "cmd": "cmd.exe",

            "explorer": "explorer.exe",
            "file explorer": "explorer.exe",

            "camera": "microsoft.windows.camera:"
        }

        executable = applications.get(app)

        if executable is None:
            print(f"Application '{app}' is not supported yet.")
            return

        try:

            if executable == "microsoft.windows.camera:":
                os.system("start microsoft.windows.camera:")

            else:
                os.startfile(executable)

            print(f"Opened: {app}")

        except Exception as e:
            print(f"Failed to open '{app}': {e}")