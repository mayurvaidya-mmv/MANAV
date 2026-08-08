"""
Capability Analyzer

Uses the local LLM to analyze missing capabilities
required to accomplish a user's goal.
"""

from ai.ai_manager import AIManager

from brain.capability_engine.capability_report import (
    CapabilityReport,
)


class CapabilityAnalyzer:

    def __init__(self):

        self.ai = AIManager()

    def analyze(self, goal: str, registry):

        report = CapabilityReport(
            goal=goal
        )

        #
        # Existing skills
        #

        for skill in registry.all_skills().values():

            metadata = skill.metadata()

            report.existing_skills.append(
                metadata.name
            )

        #
        # Ask AI to analyze missing capability
        #

        analysis = self.ai.analyze_capability(
            goal
        )

        report.missing_capabilities = analysis.get(
            "missing_capabilities",
            []
        )

        report.suggested_skill = analysis.get(
            "suggested_skill",
            "UnknownSkill"
        )

        report.estimated_complexity = analysis.get(
            "estimated_complexity",
            "Unknown"
        )

        #
        # Optional fields
        #

        report.dependencies = analysis.get(
            "dependencies",
            []
        )

        report.permissions = analysis.get(
            "permissions",
            []
        )

        report.status = "READY_FOR_DESIGN"

        return report