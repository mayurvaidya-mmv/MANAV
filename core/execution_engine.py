"""
Execution Engine

Central orchestration layer for MANAS.

Execution Flow

Request
    ↓
Planner
    ↓
Meta Agent
    ↓
Approval Layer
    ↓
Dispatcher
"""

from router.intent_classifier import IntentClassifier
from router.planner import Planner
from brain.command_parser import CommandParser

from hands.actions import ActionDispatcher

from brain.meta_agent import MetaAgent


class ExecutionEngine:

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

        self.meta_agent = MetaAgent(
            services.get("skill_registry")
        )

        self.approval = services.get(
            "approval_layer"
        )

    def execute(self, request: str):

        #
        # Intent
        #

        intent = self.classifier.classify(
            request
        )

        #
        # Plan
        #

        plan = self.planner.create_plan(
            intent,
            request
        )

        plan = self.parser.parse(plan)

        #
        # Capability Check
        #

        capability = self.meta_agent.analyze(
            plan
        )

        if capability["status"] == "MISSING":

            print()

            print("=" * 70)

            print("CAPABILITY MISSING")

            print("=" * 70)

            report = capability["report"]

            print(f"Goal : {report.goal}")

            print()

            print("Existing Skills")

            for skill in report.existing_skills:

                print(f"  ✓ {skill}")

            print()

            print("Missing Capabilities")

            for item in report.missing_capabilities:

                print(f"  • {item}")

            print()

            print(f"Suggested Skill : {report.suggested_skill}")

            print()

            return None

        #
        # Approval
        #

        if self.approval.requires_approval(plan):

            print()

            print("Approval Required.")

            return None

        #
        # Execute
        #

        return self.dispatcher.dispatch(
            plan
        )