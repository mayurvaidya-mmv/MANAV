from core.skill_registry import SkillRegistry

from skills.research_skill import ResearchSkill
from skills.application_skill import ApplicationSkill

from brain.capability_engine.analyzer import CapabilityAnalyzer


registry = SkillRegistry()

registry.register(
    ResearchSkill()
)

registry.register(
    ApplicationSkill()
)

analyzer = CapabilityAnalyzer()

report = analyzer.analyze(
    "Open WhatsApp and send Hello to Mayur",
    registry
)

print("\nGoal")
print(report.goal)

print("\nExisting Skills")

for skill in report.existing_skills:

    print("-", skill)

print("\nMissing Capabilities")

for item in report.missing_capabilities:

    print("-", item)

print("\nSuggested Skill")

print(report.suggested_skill)

print("\nComplexity")

print(report.estimated_complexity)

print("\nDependencies")

for dep in report.dependencies:

    print("-", dep)

print("\nPermissions")

for permission in report.permissions:

    print("-", permission)

print("\nStatus")

print(report.status)