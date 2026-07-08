from skills.research_skill import ResearchSkill

# Instantiate the skill
skill = ResearchSkill()

# Check metadata
print('✓ ResearchSkill instantiated')
print(f'✓ SKILL_NAME: {skill.SKILL_NAME}')
print(f'✓ SKILL_DESCRIPTION: {skill.SKILL_DESCRIPTION}')
print(f'✓ SUPPORTED_INTENTS: {skill.SUPPORTED_INTENTS}')
print(f'✓ SUPPORTED_TASKS: {skill.SUPPORTED_TASKS}')
print(f'✓ REQUIRED_INPUTS: {skill.REQUIRED_INPUTS}')
print(f'✓ OUTPUT_TYPE: {skill.OUTPUT_TYPE}')

# Test metadata() method
metadata = skill.metadata()
print(f'\n✓ metadata() returns: {metadata}')

print('\n✅ ResearchSkill metadata update successful')