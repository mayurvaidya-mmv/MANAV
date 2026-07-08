"""
hands/actions.py (REFACTORED)

Dispatches execution plans to the appropriate skills.
No longer hardcoded to specific skills.
Gates actions via ApprovalLayer.
"""


class ActionDispatcher:
    """
    Dynamically dispatches execution plans to registered skills.
    
    Instead of:
        if task == "OPEN_APPLICATION":
            return self.application.execute(plan)
    
    It now:
        skill = skill_registry.get_by_task(task)
        if skill:
            return skill.execute(plan)
    """
    
    def __init__(self, skill_registry, approval_layer):
        """
        Args:
            skill_registry: SkillRegistry instance (access to all skills)
            approval_layer: ApprovalLayer instance (gates execution)
        """
        self.skill_registry = skill_registry
        self.approval_layer = approval_layer
    
    def dispatch(self, plan: dict):
        """
        Dispatch a plan to the appropriate skill.
        
        Flow:
        1. Extract task from plan
        2. Find skill that handles this task
        3. Classify impact tier (via ApprovalLayer)
        4. Gate execution if Tier 2/3 (wait for approval)
        5. Execute the skill
        6. Return result
        
        Args:
            plan: dict with keys intent, task, arguments
        
        Returns:
            Result from skill.execute(), or error dict
        """
        
        task = plan.get("task")
        
        if not task:
            return {"error": "Plan missing 'task' field"}
        
        # Step 1: Find skill for this task
        skill = self.skill_registry.get_by_task(task)
        
        if skill is None:
            return {
                "error": f"No skill found for task: {task}",
                "available_tasks": self._list_available_tasks()
            }
        
        # Step 2: Classify the action's impact tier
        tier = self.approval_layer.classify_tier(plan, skill)
        
        print(f"[Dispatcher] Task: {task} | Tier: {tier.name} | Skill: {skill.SKILL_NAME}")
        
        # Step 3: Gate execution on approval if needed
        if self.approval_layer.needs_approval(tier):
            approved = self.approval_layer.notify_and_wait(plan, tier)
            
            if not approved:
                return {
                    "status": "pending_approval",
                    "message": f"Waiting for user approval for {task}..."
                }
        
        # Step 4: Execute the skill
        try:
            result = skill.execute(plan)
            print(f"[Dispatcher] Execution succeeded for {task}")
            return result
        
        except Exception as e:
            print(f"[Dispatcher] Execution failed: {e}")
            return {
                "error": f"Skill execution failed: {e}",
                "task": task
            }
    
    def _list_available_tasks(self) -> list:
        """List all tasks available across all registered skills."""
        tasks = []
        for metadata in self.skill_registry.list_all().values():
            tasks.extend(metadata.get("supported_tasks", []))
        return list(set(tasks))  # deduplicate