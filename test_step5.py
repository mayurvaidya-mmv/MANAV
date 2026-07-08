from core.approval_layer import ApprovalLayer, ApprovalTier

# Create approval layer
print("[TEST] Creating ApprovalLayer...\n")
approval_layer = ApprovalLayer()

# Test 1: Classify tier for different tasks
print("[TEST 1] Classify tier for different tasks:")
test_plans = [
    {"task": "OPEN_APPLICATION", "arguments": {}},
    {"task": "WEB_RESEARCH", "arguments": {}},
    {"task": "CREATE_FILE", "arguments": {}},
    {"task": "WRITE_FILE", "arguments": {}},
    {"task": "DELETE_FILE", "arguments": {}},
]

for plan in test_plans:
    tier = approval_layer.classify_tier(plan)
    print(f"  {plan['task']}: {tier.name}")

# Test 2: Check which tiers need approval
print("\n[TEST 2] Which tiers need approval:")
for tier in ApprovalTier:
    needs_approval = approval_layer.needs_approval(tier)
    print(f"  {tier.name}: {'NEEDS APPROVAL' if needs_approval else 'execute immediately'}")

# Test 3: Describe actions
print("\n[TEST 3] Describe actions:")
test_descriptions = [
    {"task": "OPEN_APPLICATION", "arguments": {"application": "chrome"}},
    {"task": "DELETE_FILE", "arguments": {"path": "/important/file.py"}},
    {"task": "WEB_RESEARCH", "arguments": {"query": "AI safety"}},
]

for plan in test_descriptions:
    description = approval_layer._describe_action(plan)
    print(f"  {description}")

print("\n✅ ApprovalLayer test successful")