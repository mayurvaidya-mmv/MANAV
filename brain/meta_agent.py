"""
Meta Agent

Determines whether MANAS already has the required
capability. If not, delegates to the Capability
Analyzer.
"""

from brain.capability_engine.analyzer import CapabilityAnalyzer


class MetaAgent:

    def __init__(self, registry):

        self.registry = registry

        self.analyzer = CapabilityAnalyzer()

    def analyze(self, plan: dict):

        task = plan.get("task", "UNKNOWN")

        for skill in self.registry.all_skills().values():

            metadata = skill.metadata()

            if task in metadata.supported_tasks:

                return {

                    "status": "FOUND",

                    "skill": skill

                }

        report = self.analyzer.analyze(
            goal=task,
            registry=self.registry
        )

        return {

            "status": "MISSING",

            "report": report

        }