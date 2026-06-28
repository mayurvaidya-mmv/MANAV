"""
MANAS Application

Top-level application container.
"""

from core.runtime import Runtime


class MANAS:

    def __init__(self):

        self.runtime = Runtime()

    def boot(self):

        self.runtime.boot()

    def process(self, request: str):

        return self.runtime.process(request)