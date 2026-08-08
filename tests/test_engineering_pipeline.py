from brain.capability_engine.capability_report import CapabilityReport
from brain.capability_engine.engineering_pipeline import EngineeringPipeline


report = CapabilityReport(

    goal="Open WhatsApp",

    suggested_skill="DesktopMessagingSkill",

    missing_capabilities=[

        "Desktop UI Automation",

        "Message Sending"

    ],

    dependencies=[

        "pywinauto"

    ]
)

pipeline = EngineeringPipeline()

pipeline.build(report)