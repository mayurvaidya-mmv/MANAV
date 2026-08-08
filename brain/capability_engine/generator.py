"""
Skill Generator

Uses the LLM to generate a new MANAS skill
from a Capability Report.
"""

from ai.ai_manager import AIManager


class SkillGenerator:

    def __init__(self):

        self.ai = AIManager()

    def generate(self, report):

        prompt = f"""
You are a Senior Python Engineer.

Generate ONE production-ready MANAS skill.

Requirements:

- Inherit from BaseSkill

- Use clean Python

- Follow PEP8

- Include metadata:

    SKILL_NAME

    SKILL_DESCRIPTION

    SUPPORTED_INTENTS

    SUPPORTED_TASKS

    REQUIRED_INPUTS

    OUTPUT_TYPE

Implement execute(plan).

Return ONLY Python.

No markdown.

No explanation.

Capability

{report.suggested_skill}

Missing Capabilities

{report.missing_capabilities}

Dependencies

{report.dependencies}
"""

        return self.ai._chat(
            prompt,
            ""
        )