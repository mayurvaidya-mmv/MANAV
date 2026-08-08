from brain.capability_engine.validator import SkillValidator


validator = SkillValidator()

code = '''
from skills.base_skill import BaseSkill

class ExampleSkill(BaseSkill):

    SKILL_NAME = "example"

    SKILL_DESCRIPTION = "Example"

    SUPPORTED_INTENTS = ["ACTION"]

    SUPPORTED_TASKS = ["TEST"]

    REQUIRED_INPUTS = []

    OUTPUT_TYPE = "dict"

    def execute(self, plan):

        return {}
'''

result = validator.validate(code)

print()

print(result)