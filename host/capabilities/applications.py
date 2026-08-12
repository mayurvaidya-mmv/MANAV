"""
Windows application capabilities.

This module contains host-side operations that interact
with applications on the Windows machine.
"""

import os


APPLICATIONS = {
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
}


def launch_application(application: str) -> bool:
    """
    Launch a supported Windows application.

    Returns True when the launch request is accepted.
    """

    name = application.strip().lower()

    executable = APPLICATIONS.get(name)

    if executable is None:
        raise ValueError(
            f"Application '{application}' is not supported."
        )

    os.startfile(executable)

    return True