from core.skill_registry import SkillRegistry

# Create registry (this will auto-discover skills)
print("[TEST] Creating SkillRegistry...\n")
registry = SkillRegistry()

# Test 1: List all skills
print("\n[TEST 1] List all skills:")
all_skills = registry.list_all()
for skill_name, metadata in all_skills.items():
    print(f"  - {skill_name}: {metadata['description']}")

# Test 2: Get skill by intent
print("\n[TEST 2] Get skill by intent:")
research_skill = registry.get_by_intent("RESEARCH")
print(f"  ✓ Skill for RESEARCH intent: {research_skill.SKILL_NAME if research_skill else 'NOT FOUND'}")

action_skill = registry.get_by_intent("ACTION")
print(f"  ✓ Skill for ACTION intent: {action_skill.SKILL_NAME if action_skill else 'NOT FOUND'}")

# Test 3: Get skill by task
print("\n[TEST 3] Get skill by task:")
web_research_skill = registry.get_by_task("WEB_RESEARCH")
print(f"  ✓ Skill for WEB_RESEARCH task: {web_research_skill.SKILL_NAME if web_research_skill else 'NOT FOUND'}")

open_app_skill = registry.get_by_task("OPEN_APPLICATION")
print(f"  ✓ Skill for OPEN_APPLICATION task: {open_app_skill.SKILL_NAME if open_app_skill else 'NOT FOUND'}")

# Test 4: Check manifest was created
print("\n[TEST 4] Check skill_manifest.json:")
from pathlib import Path
manifest_file = Path("skills/skill_manifest.json")
if manifest_file.exists():
    print(f"  ✓ skill_manifest.json created at: {manifest_file.absolute()}")
    import json
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)
        print(f"  ✓ Contains {len(manifest)} skill(s)")
else:
    print(f"  ✗ skill_manifest.json NOT found")

print("\n✅ SkillRegistry test successful")