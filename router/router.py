"""
router/router.py
"""

from router.intent_classifier import IntentClassifier
from router.planner import Planner
from brain.command_parser import CommandParser

from hands.actions import ActionDispatcher


class Router:

    def __init__(self, services):

        self.services = services

        self.classifier = IntentClassifier()

        self.planner = Planner(
            services
        )

        self.parser = CommandParser()

        self.dispatcher = ActionDispatcher(
            services
        )

    def route(self, request: str):

        intent = self.classifier.classify(request)

        plan = self.planner.create_plan(
            intent,
            request
        )

        plan = self.parser.parse(plan)

        result = self.dispatcher.dispatch(plan)

        return result