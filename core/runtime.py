"""
MANAS Runtime

Boots all MANAS services.
"""

from router.router import Router
from core.services import ServiceRegistry
from core.events import EventBus

class Runtime:

    def __init__(self):

        self.services = ServiceRegistry()

    def boot(self):
        
        print("Booting Runtime...\n")
        event_bus = EventBus()

        self.services.register(
            "event_bus",
            event_bus
        )

        print("✓ Event Bus")


        router = Router()

        self.services.register(
            "router",
            router
        )

        print("✓ Router")

        print("\nRuntime Ready.\n")

    def process(self, request: str):

        router = self.services.get("router")

        return router.route(request)