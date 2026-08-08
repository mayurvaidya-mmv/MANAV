"""
Output Cleaner

Cleans LLM-generated code before validation.
"""


class OutputCleaner:

    def clean(self, code: str):

        code = code.strip()

        if code.startswith("```python"):

            code = code[len("```python"):]

        if code.startswith("```"):

            code = code[len("```"):]

        if code.endswith("```"):

            code = code[:-3]

        return code.strip()