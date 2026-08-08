from brain.capability_engine.registrar import SkillRegistrar


registrar = SkillRegistrar()

code = """
class ExampleSkill:

    pass
"""

path = registrar.register(

    "example_skill",

    code

)

print()

print("Saved to:")

print(path)