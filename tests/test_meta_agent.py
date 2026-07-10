from brain.meta_agent import MetaAgent

from core.skill_registry import SkillRegistry

from skills.research_skill import ResearchSkill
from skills.application_skill import ApplicationSkill


registry = SkillRegistry()

registry.register(
    ResearchSkill()
)

registry.register(
    ApplicationSkill()
)

agent = MetaAgent(
    registry
)

plans = [

    {
        "task": "WEB_RESEARCH"
    },

    {
        "task": "OPEN_APPLICATION"
    },

    {
        "task": "DELETE_FILES"
    }

]

for plan in plans:

    result = agent.analyze(plan)

    print(plan["task"])

    print(result)

    print("-" * 40)