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
    "Open WhatsApp and send Hello",
    registry
)

print()

print("Goal")

print(report.goal)

print()

print("Existing Skills")

for skill in report.existing_skills:

    print("-", skill)

print()

print("Missing")

for capability in report.missing_capabilities:

    print("-", capability)

print()

print("Suggested Skill")

print(report.suggested_skill)

print()

print("Status")

print(report.status)