"""
MANAS Runtime

Boots all MANAS services.
"""

from core.services import ServiceRegistry
from core.events import EventBus
from core.logger import Logger
from core.config import Config
from core.skill_registry import SkillRegistry
from core.approval_layer import ApprovalLayer
from core.execution_engine import ExecutionEngine

from skills.research_skill import ResearchSkill
from skills.application_skill import ApplicationSkill


class Runtime:

    def __init__(self):

        self.services = ServiceRegistry()

    def boot(self):

        print("Booting Runtime...\n")

        #
        # Logger
        #

        logger = Logger()

        self.services.register(
            "logger",
            logger
        )

        logger.info("Logger initialized.")

        #
        # Configuration
        #

        config = Config()

        self.services.register(
            "config",
            config
        )

        logger.info("Configuration initialized.")

        #
        # Event Bus
        #

        event_bus = EventBus()

        self.services.register(
            "event_bus",
            event_bus
        )

        logger.info("Event Bus initialized.")

        #
        # Skill Registry
        #

        skill_registry = SkillRegistry()

        skill_registry.register(
            ResearchSkill()
        )

        skill_registry.register(
            ApplicationSkill()
        )

        self.services.register(
            "skill_registry",
            skill_registry
        )

        logger.info("Skill Registry initialized.")

        #
        # Approval Layer
        #

        approval_layer = ApprovalLayer()

        self.services.register(
            "approval_layer",
            approval_layer
        )

        logger.info("Approval Layer initialized.")

        #
        # Execution Engine
        #

        engine = ExecutionEngine(
            self.services
        )

        self.services.register(
            "execution_engine",
            engine
        )

        logger.info("Execution Engine initialized.")

        logger.info("Runtime Ready.")

    def process(self, request: str):

        engine = self.services.get(
            "execution_engine"
        )

        return engine.execute(
            request
        )