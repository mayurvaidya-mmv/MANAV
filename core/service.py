"""
Base Service

All MANAS services inherit from this.
"""


class Service:

    def __init__(self, services):

        self.services = services

    @property
    def logger(self):

        return self.services.get("logger")

    @property
    def config(self):

        return self.services.get("config")

    @property
    def event_bus(self):

        return self.services.get("event_bus")