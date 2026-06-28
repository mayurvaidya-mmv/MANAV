"""
MANAS Runtime

Boots all MANAS services.
"""

from router.router import Router
from core.services import ServiceRegistry
from core.events import EventBus
from core.logger import Logger

class Runtime:

    def __init__(self):

        self.services = ServiceRegistry()

    def boot(self):
        logger = Logger()

        self.services.register(

            "logger",

            logger

        )

        logger.info("Logger initialized.")


        print("Booting Runtime...\n")
        event_bus = EventBus()

        self.services.register(
            "event_bus",
            event_bus
        )

        logger.info("Event Bus initialized.")


        router = Router()

        self.services.register(
            "router",
            router
        )

        logger.info("Router initialized.")

        logger.info("Runtime Ready.")

    def process(self, request: str):

        router = self.services.get("router")

        return router.route(request)