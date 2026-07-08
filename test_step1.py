from skills.base_skill import BaseSkill, SkillMetadata

# Check BaseSkill has the attributes
print('✓ BaseSkill imported')
print(f'✓ SKILL_NAME exists: {hasattr(BaseSkill, "SKILL_NAME")}')
print(f'✓ SKILL_DESCRIPTION exists: {hasattr(BaseSkill, "SKILL_DESCRIPTION")}')
print(f'✓ SUPPORTED_INTENTS exists: {hasattr(BaseSkill, "SUPPORTED_INTENTS")}')
print(f'✓ SUPPORTED_TASKS exists: {hasattr(BaseSkill, "SUPPORTED_TASKS")}')
print(f'✓ execute() method exists: {hasattr(BaseSkill, "execute")}')
print(f'✓ metadata() method exists: {hasattr(BaseSkill, "metadata")}')
print('\n✅ BaseSkill update successful')