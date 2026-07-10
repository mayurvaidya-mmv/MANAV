"""
Capability Analyzer

Analyzes whether an execution plan can be fulfilled
using existing MANAS capabilities.
"""

from brain.capability_engine.capability_report import CapabilityReport


class CapabilityAnalyzer:

    def analyze(self, goal: str, registry):

        report = CapabilityReport(goal=goal)

        #
        # Existing skills
        #

        for skill in registry.all_skills().values():

            metadata = skill.metadata()

            report.existing_skills.append(
                metadata.name
            )

        #
        # Temporary placeholder.
        #
        # Later this section will use the LLM
        # to infer missing capabilities.
        #

        report.missing_capabilities.append(
            "Capability analysis not yet implemented."
        )

        report.suggested_skill = "Unknown"

        report.estimated_complexity = "Unknown"

        report.status = "READY_FOR_DESIGN"

        return report