from brain.capability_engine.generator import SkillGenerator
from brain.capability_engine.capability_report import CapabilityReport


report = CapabilityReport(

    goal="Open WhatsApp",

    suggested_skill="DesktopMessagingSkill",

    missing_capabilities=[

        "Desktop UI Automation",

        "WhatsApp Interaction",

        "Message Sending"

    ],

    dependencies=[

        "pywinauto"

    ]
)

generator = SkillGenerator()

code = generator.generate(report)

print()

print("=" * 80)

print(code)

print("=" * 80)