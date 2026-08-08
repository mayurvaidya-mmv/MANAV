"""
Skill Validator

Validates AI-generated MANAS skills.
"""

import ast


class SkillValidator:

    REQUIRED_ATTRIBUTES = [

        "SKILL_NAME",

        "SKILL_DESCRIPTION",

        "SUPPORTED_INTENTS",

        "SUPPORTED_TASKS",

        "REQUIRED_INPUTS",

        "OUTPUT_TYPE"

    ]

    def validate(self, code: str):

        try:

            tree = ast.parse(code)

        except SyntaxError as e:

            return {

                "valid": False,

                "reason": f"Syntax Error: {e}"

            }

        class_found = False

        baseskill_found = False

        execute_found = False

        attributes = set()

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                class_found = True

                for base in node.bases:

                    if getattr(base, "id", "") == "BaseSkill":

                        baseskill_found = True

                for item in node.body:

                    if isinstance(item, ast.FunctionDef):

                        if item.name == "execute":

                            execute_found = True

                    if isinstance(item, ast.Assign):

                        for target in item.targets:

                            if isinstance(target, ast.Name):

                                attributes.add(target.id)

        if not class_found:

            return {

                "valid": False,

                "reason": "No class found."

            }

        if not baseskill_found:

            return {

                "valid": False,

                "reason": "Skill must inherit BaseSkill."

            }

        if not execute_found:

            return {

                "valid": False,

                "reason": "execute() method missing."

            }

        missing = []

        for attr in self.REQUIRED_ATTRIBUTES:

            if attr not in attributes:

                missing.append(attr)

        if missing:

            return {

                "valid": False,

                "reason": f"Missing metadata: {missing}"

            }

        return {

            "valid": True,

            "reason": "Skill validated successfully."

        }