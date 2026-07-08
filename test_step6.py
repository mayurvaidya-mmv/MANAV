from brain.meta_agent import MetaAgent
from core.skill_registry import SkillRegistry

# We need a mock LLM service for testing
class MockLLMService:
    """Mock LLM that returns pre-defined responses."""
    
    def query(self, prompt: str) -> str:
        """Return a mock response."""
        if "describe a NEW skill" in prompt:
            return """
- Name: file_operations
- Description: Read, write, and manage files on the system
- Tasks it handles: READ_FILE, WRITE_FILE, CREATE_FILE
- Inputs: path, content (for write)
- Output: dict with status and result
"""
        elif "Generate ONLY the Python code" in prompt:
            return '''
from skills.base_skill import BaseSkill

class FileOperationsSkill(BaseSkill):
    SKILL_NAME = "file_operations"
    SKILL_DESCRIPTION = "Read, write, and manage files"
    SUPPORTED_INTENTS = ["ACTION"]
    SUPPORTED_TASKS = ["READ_FILE", "WRITE_FILE", "CREATE_FILE"]
    REQUIRED_INPUTS = ["path"]
    OUTPUT_TYPE = "dict"
    
    def execute(self, plan: dict):
        task = plan.get("task")
        args = plan.get("arguments", {})
        
        if task == "READ_FILE":
            try:
                with open(args.get("path"), "r") as f:
                    content = f.read()
                return {"status": "success", "content": content}
            except Exception as e:
                return {"status": "error", "error": str(e)}
        
        return {"status": "error", "error": f"Unknown task: {task}"}
'''
        return ""

# Test
print("[TEST] Creating MetaAgent...\n")

# Create registry and mock LLM
registry = SkillRegistry()
mock_llm = MockLLMService()

# Create MetaAgent
meta_agent = MetaAgent(mock_llm, registry)
print("✓ MetaAgent created")

# Test that methods exist
print(f"✓ generate_skill method exists: {hasattr(meta_agent, 'generate_skill')}")
print(f"✓ _describe_needed_skill method exists: {hasattr(meta_agent, '_describe_needed_skill')}")
print(f"✓ _generate_skill_code method exists: {hasattr(meta_agent, '_generate_skill_code')}")
print(f"✓ _build_metadata method exists: {hasattr(meta_agent, '_build_metadata')}")
print(f"✓ _instantiate_skill method exists: {hasattr(meta_agent, '_instantiate_skill')}")

print("\n✅ MetaAgent test successful")