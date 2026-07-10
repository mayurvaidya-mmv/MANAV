"""
Approval Layer

Determines whether a plan can be executed
immediately or requires user approval.
"""


class ApprovalLayer:

    #
    # Task → Approval Tier
    #
    # Tier 0 : Safe
    # Tier 1 : Low Risk
    # Tier 2 : Medium Risk
    # Tier 3 : High Risk
    #

    TASK_TIER_MAP = {

        #
        # Safe operations
        #

        "WEB_RESEARCH": 0,

        "CHAT": 0,

        "OPEN_APPLICATION": 0,

    }

    def classify(self, plan: dict) -> int:
        """
        Return the approval tier for a plan.
        """

        task = plan.get("task", "UNKNOWN")

        return self.TASK_TIER_MAP.get(task, 3)

    def requires_approval(self, plan: dict) -> bool:
        """
        Determine whether approval is required.
        """

        tier = self.classify(plan)

        return tier >= 2