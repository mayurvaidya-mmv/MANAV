from core.skill_registry import SkillRegistry

from skills.research_skill import ResearchSkill
from skills.application_skill import ApplicationSkill


registry = SkillRegistry()

registry.register(ResearchSkill())
registry.register(ApplicationSkill())

print()

print("Registered Skills")

print("-" * 40)

for name in registry.list_names():

    print(name)

print()

print("Metadata")

print("-" * 40)

for name, metadata in registry.metadata().items():

    print(metadata)