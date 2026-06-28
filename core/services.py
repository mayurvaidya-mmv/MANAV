"""
Service Registry

Stores shared MANAS services.
"""


class ServiceRegistry:

    def __init__(self):

        self._services = {}

    def register(self, name: str, service):

        self._services[name] = service

    def get(self, name: str):

        return self._services[name]

    def exists(self, name: str):

        return name in self._services