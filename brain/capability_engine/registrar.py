"""
Skill Registrar

Responsible for saving AI-generated skills
into the MANAS project.
"""

from pathlib import Path


class SkillRegistrar:

    def __init__(self):

        self.output_dir = Path("skills/generated")

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def register(self, skill_name: str, code: str):

        filename = f"{skill_name}.py"

        filepath = self.output_dir / filename

        filepath.write_text(
            code,
            encoding="utf-8"
        )

        return filepath