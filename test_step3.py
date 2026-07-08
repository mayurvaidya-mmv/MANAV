from skills.application_skill import ApplicationSkill

# Instantiate the skill
skill = ApplicationSkill()

# Check metadata
print('✓ ApplicationSkill instantiated')
print(f'✓ SKILL_NAME: {skill.SKILL_NAME}')
print(f'✓ SKILL_DESCRIPTION: {skill.SKILL_DESCRIPTION}')
print(f'✓ SUPPORTED_INTENTS: {skill.SUPPORTED_INTENTS}')
print(f'✓ SUPPORTED_TASKS: {skill.SUPPORTED_TASKS}')
print(f'✓ REQUIRED_INPUTS: {skill.REQUIRED_INPUTS}')
print(f'✓ OUTPUT_TYPE: {skill.OUTPUT_TYPE}')

# Test metadata() method
metadata = skill.metadata()
print(f'\n✓ metadata() works: {metadata.name}')

print('\n✅ ApplicationSkill metadata update successful')