"""
Dynamic Skill Registry

Stores and retrieves all available MANAS skills.

V4.2:
- Manual registration
- Skill lookup
- Metadata access
"""

from skills.base_skill import BaseSkill


class SkillRegistry:

    def __init__(self):

        self._skills = {}

    def register(self, skill: BaseSkill):
        """
        Register a skill instance.
        """

        metadata = skill.metadata()

        self._skills[metadata.name] = skill

    def get(self, name: str):
        """
        Retrieve a registered skill by name.
        """

        return self._skills.get(name)

    def exists(self, name: str) -> bool:
        """
        Check if a skill exists.
        """

        return name in self._skills

    def all_skills(self):
        """
        Return all registered skills.
        """

        return self._skills

    def list_names(self):
        """
        Return registered skill names.
        """

        return list(self._skills.keys())

    def metadata(self):
        """
        Return metadata for every registered skill.
        """

        return {
            name: skill.metadata()
            for name, skill in self._skills.items()
        }