from core.approval_layer import ApprovalLayer

approval = ApprovalLayer()

plans = [

    {
        "task": "WEB_RESEARCH"
    },

    {
        "task": "OPEN_APPLICATION"
    },

    {
        "task": "DELETE_FILES"
    }

]

for plan in plans:

    tier = approval.classify(plan)

    print(plan["task"])

    print("Tier:", tier)

    print(
        "Requires Approval:",
        approval.requires_approval(plan)
    )

    print("-" * 40)