"""
Engineering Pipeline

Coordinates the autonomous engineering workflow.
"""

from brain.capability_engine.generator import SkillGenerator
from brain.capability_engine.validator import SkillValidator
from brain.capability_engine.registrar import SkillRegistrar
from brain.capability_engine.output_cleaner import OutputCleaner

class EngineeringPipeline:

    def __init__(self):

        self.generator = SkillGenerator()

        self.validator = SkillValidator()

        self.registrar = SkillRegistrar()

        self.cleaner = OutputCleaner()

    def build(self, report):

        print()

        print("=" * 70)
        print("ENGINEERING PIPELINE")
        print("=" * 70)

        #
        # Generate
        #

        print("\n[1/3] Generating Skill...")

        code = self.generator.generate(report)

        code = self.cleaner.clean(code)
        
        print()

        print("=" * 80)
        print("GENERATED CODE")
        print("=" * 80)

        print(code)

        print("=" * 80)
        #
        # Validate
        #

        print("[2/3] Validating Skill...")

        validation = self.validator.validate(code)

        if not validation["valid"]:

            print()

            print("Validation Failed")

            print(validation["reason"])

            return None

        #
        # Register
        #

        print("[3/3] Registering Skill...")

        filename = report.suggested_skill

        path = self.registrar.register(

            filename,

            code

        )

        print()

        print("Skill Registered Successfully")

        print(path)

        return path