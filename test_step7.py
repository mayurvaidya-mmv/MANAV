from router.planner import Planner
from router.intent_types import Intent
from core.skill_registry import SkillRegistry
from core.approval_layer import ApprovalLayer
from brain.meta_agent import MetaAgent

# Mock LLM for testing
class MockLLMService:
    def query(self, prompt: str) -> str:
        return "Mock response"

# Test
print("[TEST] Creating Planner with dependencies...\n")

# Create dependencies
registry = SkillRegistry()
approval_layer = ApprovalLayer()
mock_llm = MockLLMService()
meta_agent = MetaAgent(mock_llm, registry)

# Create Planner
planner = Planner(registry, meta_agent, approval_layer)
print("✓ Planner created with SkillRegistry, MetaAgent, ApprovalLayer")

# Test 1: Plan for RESEARCH intent (should find ResearchSkill)
print("\n[TEST 1] Plan for RESEARCH intent:")
plan = planner.create_plan(Intent.RESEARCH, "research machine learning")
print(f"  Task: {plan.get('task')}")
print(f"  Arguments: {plan.get('arguments')}")

# Test 2: Plan for ACTION intent (should find ApplicationSkill)
print("\n[TEST 2] Plan for ACTION intent:")
plan = planner.create_plan(Intent.ACTION, "open chrome")
print(f"  Task: {plan.get('task')}")
print(f"  Arguments: {plan.get('arguments')}")

# Test 3: Plan for CHAT intent (no skill, but should handle gracefully)
print("\n[TEST 3] Plan for CHAT intent (no skill):")
plan = planner.create_plan(Intent.CHAT, "what is AI?")
print(f"  Task: {plan.get('task')}")
print(f"  Arguments: {plan.get('arguments')}")

print("\n✅ Planner test successful")