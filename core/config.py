"""
MANAS Configuration Service.
"""

from config.settings import *


class Config:

    def __init__(self):

        self.whisper_model = WHISPER_MODEL
        self.whisper_device = WHISPER_DEVICE
        self.whisper_compute_type = WHISPER_COMPUTE_TYPE

        self.debug = DEBUG

    def __str__(self):

        return (
            f"Whisper Model : {self.whisper_model}\n"
            f"Device         : {self.whisper_device}\n"
            f"Compute Type   : {self.whisper_compute_type}\n"
            f"Debug          : {self.debug}"
        )