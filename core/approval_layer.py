"""
core/approval_layer.py

Gates execution of consequential actions.
Classifies actions into Tier 0-3 based on reversibility/impact.
"""

import time
from enum import Enum
from datetime import datetime
from typing import Optional, Dict


class ApprovalTier(Enum):
    """Impact classification for actions."""
    TIER_0 = 0  # Reversible, read-only — execute immediately
    TIER_1 = 1  # Reversible, visible — execute immediately, log
    TIER_2 = 2  # Consequential, hard to reverse — needs approval
    TIER_3 = 3  # Irreversible, high-stakes — needs approval + confirmation


class ApprovalLayer:
    """
    Reviews and gates actions based on their impact tier.
    Manages user notifications and approval requests.
    """
    
    def __init__(self, notification_manager=None):
        self.notification_manager = notification_manager
        self.pending_approvals = {}  # {id: {"plan": ..., "approved": True/False/None, ...}}
        self.approval_history = []
        
        # Task type → Tier mapping
        self.task_tier_map = {
            # TIER 0 — read-only, reversible
            "OPEN_APPLICATION": ApprovalTier.TIER_0,
            "READ_FILE": ApprovalTier.TIER_0,
            "WEB_RESEARCH": ApprovalTier.TIER_0,
            "CHAT": ApprovalTier.TIER_0,
            "SCREENSHOT": ApprovalTier.TIER_0,
            
            # TIER 1 — visible but reversible
            "CREATE_FILE": ApprovalTier.TIER_1,
            "CREATE_FOLDER": ApprovalTier.TIER_1,
            
            # TIER 2 — consequential, hard to reverse
            "WRITE_FILE": ApprovalTier.TIER_2,
            "EDIT_FILE": ApprovalTier.TIER_2,
            "MOVE_FILE": ApprovalTier.TIER_2,
            "RUN_CODE": ApprovalTier.TIER_2,
            "EXECUTE_COMMAND": ApprovalTier.TIER_2,
            
            # TIER 3 — irreversible
            "DELETE_FILE": ApprovalTier.TIER_3,
            "DELETE_FOLDER": ApprovalTier.TIER_3,
            "MODIFY_SKILL_CODE": ApprovalTier.TIER_3,
            "PUSH_TO_GIT": ApprovalTier.TIER_3,
            "INSTALL_PACKAGE": ApprovalTier.TIER_3,
        }
    
    def classify_tier(self, plan: dict, skill=None) -> ApprovalTier:
        """
        Classify the impact tier of a planned action.
        
        Args:
            plan: dict with keys task, arguments
            skill: the skill that will execute (optional)
        
        Returns:
            ApprovalTier enum value
        """
        task = plan.get("task", "UNKNOWN")
        
        # First try the task_tier_map
        if task in self.task_tier_map:
            return self.task_tier_map[task]
        
        # Skill-specific tier classification (if available)
        if skill and hasattr(skill, 'classify_tier'):
            result = skill.classify_tier(plan)
            if result is not None:
                return result
        
        # Default: be conservative, require approval for unknown tasks
        return ApprovalTier.TIER_2
    
    def needs_approval(self, tier: ApprovalTier) -> bool:
        """Check if an action at this tier needs approval."""
        return tier in [ApprovalTier.TIER_2, ApprovalTier.TIER_3]
    
    def notify_and_wait(self, plan: dict, tier: ApprovalTier, timeout_seconds: int = 300) -> bool:
        """
        Notify user of a consequential action and wait for approval.
        
        Args:
            plan: the execution plan
            tier: the approval tier
            timeout_seconds: how long to wait before timing out
        
        Returns:
            True if approved, False if rejected or timed out
        """
        
        # Generate a unique ID for this approval request
        approval_id = f"approval_{datetime.now().timestamp()}_{id(plan)}"
        
        # Describe the action clearly
        action_description = self._describe_action(plan)
        
        # Store the pending approval
        self.pending_approvals[approval_id] = {
            "plan": plan,
            "tier": tier,
            "description": action_description,
            "approved": None,
            "created_at": datetime.now(),
            "timeout_seconds": timeout_seconds
        }
        
        # Notify user across channels
        if self.notification_manager:
            self.notification_manager.send_approval_request(
                approval_id=approval_id,
                description=action_description,
                tier=tier,
                timeout_seconds=timeout_seconds
            )
        else:
            # Fallback: print to console
            self._print_approval_request(approval_id, action_description, tier)
        
        # Wait for approval
        approved = self._wait_for_approval(approval_id, timeout_seconds)
        
        # Record in history
        self.approval_history.append({
            "approval_id": approval_id,
            "description": action_description,
            "tier": tier.name,
            "approved": approved,
            "timestamp": datetime.now().isoformat()
        })
        
        return approved
    
    def _describe_action(self, plan: dict) -> str:
        """
        Describe what the action will do in human-readable terms.
        """
        task = plan.get("task", "UNKNOWN")
        args = plan.get("arguments", {})
        
        descriptions = {
            "OPEN_APPLICATION": f"Open application: {args.get('application', 'unknown')}",
            "READ_FILE": f"Read file: {args.get('path', 'unknown')}",
            "CREATE_FILE": f"Create file: {args.get('path', 'unknown')}",
            "WRITE_FILE": f"Write to file: {args.get('path', 'unknown')} ({len(str(args.get('content', '')))} chars)",
            "EDIT_FILE": f"Edit file: {args.get('path', 'unknown')}",
            "DELETE_FILE": f"DELETE file: {args.get('path', 'unknown')} — THIS CANNOT BE UNDONE",
            "DELETE_FOLDER": f"DELETE folder: {args.get('path', 'unknown')} — THIS CANNOT BE UNDONE",
            "RUN_CODE": f"Execute code: {str(args.get('code', ''))[:100]}...",
            "PUSH_TO_GIT": f"Push to Git repository with message: {args.get('message', '')}",
            "WEB_RESEARCH": f"Research: {args.get('query', 'unknown')}",
        }
        
        return descriptions.get(task, f"Execute task: {task}")
    
    def _print_approval_request(self, approval_id: str, description: str, tier: ApprovalTier):
        """Fallback approval printing to console."""
        tier_str = "HIGH-STAKES" if tier == ApprovalTier.TIER_3 else "CONSEQUENTIAL"
        
        print("\n" + "="*70)
        print(f"⚠️  {tier_str} ACTION REQUIRES APPROVAL")
        print("="*70)
        print(f"ID: {approval_id}")
        print(f"Action: {description}")
        print("="*70)
        print(f"Approve? Type: approve {approval_id}")
        print(f"Reject? Type: reject {approval_id}")
        print("="*70 + "\n")
    
    def _wait_for_approval(self, approval_id: str, timeout_seconds: int) -> bool:
        """
        Wait for approval. Check every 0.5 seconds.
        Return False on timeout.
        """
        start = time.time()
        
        while time.time() - start < timeout_seconds:
            if self.pending_approvals[approval_id]["approved"] is not None:
                approved = self.pending_approvals[approval_id]["approved"]
                print(f"[ApprovalLayer] Action {approval_id}: {'APPROVED' if approved else 'REJECTED'}")
                return approved
            
            time.sleep(0.5)
        
        # Timeout
        print(f"[ApprovalLayer] Action {approval_id}: TIMEOUT (no response in {timeout_seconds}s)")
        return False
    
    def approve_action(self, approval_id: str):
        """Called when user approves an action."""
        if approval_id in self.pending_approvals:
            self.pending_approvals[approval_id]["approved"] = True
            print(f"[ApprovalLayer] Approved: {approval_id}")
    
    def reject_action(self, approval_id: str):
        """Called when user rejects an action."""
        if approval_id in self.pending_approvals:
            self.pending_approvals[approval_id]["approved"] = False
            print(f"[ApprovalLayer] Rejected: {approval_id}")
    
    def review_generated_skill(self, skill_code: dict) -> bool:
        """
        Review auto-generated skill code before registration.
        
        Args:
            skill_code: dict with:
                - class_definition: str of Python code
                - metadata: dict with skill metadata
        
        Returns:
            True if approved, False if rejected
        """
        
        print("\n" + "="*70)
        print("✨ NEW SKILL AUTO-GENERATED")
        print("="*70)
        print(f"Name: {skill_code['metadata'].get('name', 'unknown')}")
        print(f"Description: {skill_code['metadata'].get('description', '')}")
        print(f"Supported Tasks: {skill_code['metadata'].get('supported_tasks', [])}")
        print("="*70)
        print("Generated Code:")
        print("-"*70)
        
        code_preview = skill_code['class_definition']
        if len(code_preview) > 1000:
            print(code_preview[:1000] + "\n... [truncated]")
        else:
            print(code_preview)
        
        print("="*70)
        print("Review this code carefully.")
        print("Approve this skill? (yes/no): ", end="")
        
        response = input().strip().lower()
        approved = response == "yes"
        
        return approved