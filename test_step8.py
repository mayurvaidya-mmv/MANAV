from hands.actions import ActionDispatcher
from core.skill_registry import SkillRegistry
from core.approval_layer import ApprovalLayer

print("[TEST] Creating ActionDispatcher...\n")

# Create dependencies
registry = SkillRegistry()
approval_layer = ApprovalLayer()

# Create dispatcher
dispatcher = ActionDispatcher(registry, approval_layer)
print("✓ ActionDispatcher created\n")

# Test 1: Dispatch a WEB_RESEARCH task
print("[TEST 1] Dispatch WEB_RESEARCH task (TIER_0 - no approval needed):")
plan = {
    "intent": "RESEARCH",
    "task": "WEB_RESEARCH",
    "arguments": {"query": "machine learning"}
}
result = dispatcher.dispatch(plan)
print(f"  Result: {result}\n")

# Test 2: Dispatch OPEN_APPLICATION task
print("[TEST 2] Dispatch OPEN_APPLICATION task (TIER_0 - no approval needed):")
plan = {
    "intent": "ACTION",
    "task": "OPEN_APPLICATION",
    "arguments": {"application": "chrome"}
}
result = dispatcher.dispatch(plan)
print(f"  Result: {result}\n")

# Test 3: Dispatch unknown task
print("[TEST 3] Dispatch unknown task (should fail gracefully):")
plan = {
    "intent": "UNKNOWN",
    "task": "UNKNOWN_TASK",
    "arguments": {}
}
result = dispatcher.dispatch(plan)
print(f"  Result: {result}\n")

# Test 4: List available tasks
print("[TEST 4] List available tasks:")
available_tasks = dispatcher._list_available_tasks()
for task in available_tasks:
    print(f"  - {task}")

print("\n✅ ActionDispatcher test successful")