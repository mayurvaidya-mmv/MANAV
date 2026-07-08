"""
router/planner.py (REFACTORED)

Creates execution plans dynamically based on available skills.
Triggers Meta-Agent when no skill exists for the intent.
"""

from router.intent_types import Intent


class Planner:
    """
    Plans task execution based on classified intents.
    
    Instead of hardcoding task mappings, queries the SkillRegistry:
    - Do we have a skill for this intent?
    - If yes, ask the skill to plan the task
    - If no, trigger Meta-Agent to create one
    """
    
    def __init__(self, skill_registry, meta_agent, approval_layer):
        """
        Args:
            skill_registry: SkillRegistry instance
            meta_agent: MetaAgent instance (generates skills)
            approval_layer: ApprovalLayer instance (gates execution)
        """
        self.skill_registry = skill_registry
        self.meta_agent = meta_agent
        self.approval_layer = approval_layer
    
    def create_plan(self, intent: Intent, request: str):
        """
        Create an execution plan for the given intent and request.
        
        Flow:
        1. Check if we have a skill for this intent
        2. If no skill → trigger Meta-Agent to generate one
        3. Ask the skill to plan the execution
        4. Return the plan
        
        Args:
            intent: Intent enum (from classifier)
            request: Raw user request string
        
        Returns:
            dict with structure:
                {
                    "intent": str,
                    "task": str,
                    "arguments": dict
                }
            OR error dict if generation/approval failed
        """
        
        request = request.strip()
        
        # Step 1: Check if we have a skill for this intent
        skill = self.skill_registry.get_by_intent(intent.name)
        
        if skill is None:
            # Step 2: No skill found — trigger Meta-Agent
            print(f"\n[Planner] No skill found for intent: {intent.name}")
            print(f"[Planner] Triggering Meta-Agent to generate a new skill...\n")
            
            skill = self._generate_and_register_skill(intent, request)
            
            if skill is None:
                return {
                    "error": f"Failed to generate skill for intent: {intent.name}"
                }
        
        # Step 3: Ask the skill to plan the execution
        try:
            plan = self._ask_skill_to_plan(skill, intent, request)
            return plan
        except Exception as e:
            print(f"[Planner] Error planning with skill: {e}")
            return {"error": str(e)}
    
    def _generate_and_register_skill(self, intent: Intent, request: str):
        """
        Generate a new skill via Meta-Agent and register it.
        
        Returns:
            The registered skill instance, or None if failed
        """
        
        # Generate
        generated = self.meta_agent.generate_skill(intent, request, self.skill_registry)
        
        if generated is None:
            print("[Planner] Meta-Agent failed to generate skill")
            return None
        
        # Get approval
        approved = self.approval_layer.review_generated_skill(generated)
        
        if not approved:
            print("[Planner] User rejected the generated skill")
            return None
        
        # Register
        success = self.skill_registry.register_dynamic(
            generated["instance"].__class__,
            generated["metadata"]
        )
        
        if success:
            print(f"[Planner] Registered new skill: {generated['metadata']['name']}")
            return generated["instance"]
        else:
            print("[Planner] Failed to register generated skill")
            return None
    
    def _ask_skill_to_plan(self, skill, intent: Intent, request: str) -> dict:
        """
        Ask a skill how it would plan this request.
        
        This allows skills to decide what tasks to run based on the intent/request.
        Simple skills may return a fixed task; complex ones may branch logic.
        """
        
        # Ask the skill: given this intent and request, what plan would you create?
        # For now, we'll use a simple heuristic:
        
        # If the skill has a plan() method, call it
        if hasattr(skill, 'plan'):
            return skill.plan(intent, request)
        
        # Otherwise, map intent → task automatically
        # This is a fallback for skills that don't implement plan()
        
        plan = self._default_plan_for_intent(intent, request, skill)
        return plan
    
    def _default_plan_for_intent(self, intent: Intent, request: str, skill) -> dict:
        """
        Default plan generation for standard intents.
        Used as fallback if skill doesn't implement plan().
        """
        
        if intent == Intent.ACTION:
            return {
                "intent": intent.name,
                "task": "OPEN_APPLICATION",
                "arguments": {
                    "application": request.replace("open", "").strip().lower()
                }
            }
        
        if intent == Intent.RESEARCH:
            return {
                "intent": intent.name,
                "task": "WEB_RESEARCH",
                "arguments": {
                    "query": request
                }
            }
        
        if intent == Intent.CHAT:
            return {
                "intent": intent.name,
                "task": "CHAT",
                "arguments": {
                    "message": request
                }
            }
        
        # Fallback for unknown intent
        return {
            "intent": intent.name,
            "task": "UNKNOWN",
            "arguments": {}
        }