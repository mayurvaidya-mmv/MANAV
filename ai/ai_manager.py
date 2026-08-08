"""
AI Manager

Central interface to the local LLM.
"""

import json
import requests

from config.settings import LOCAL_LLM_HOST
from config.settings import LOCAL_MODEL
from config.settings import DEBUG

from ai.prompts import (
    INTENT_CLASSIFIER_PROMPT,
    CAPABILITY_ANALYZER_PROMPT,
)

from knowledge.parser import KnowledgeParser
from core.logger import Logger


class AIManager:

    def __init__(self):

        self.url = f"{LOCAL_LLM_HOST}/v1/chat/completions"

        self.model = LOCAL_MODEL

        self.parser = KnowledgeParser()

        self.logger = Logger()

    def _chat(self, system_prompt: str, user_prompt: str):

        response = requests.post(

            self.url,

            json={

                "model": self.model,

                "messages": [

                    {
                        "role": "system",
                        "content": system_prompt
                    },

                    {
                        "role": "user",
                        "content": user_prompt
                    }

                ],

                "temperature": 0

            }

        )

        if response.status_code != 200:

            print()

            print("=" * 80)

            print("LM STUDIO ERROR")

            print(response.status_code)

            print(response.text)

            print("=" * 80)

            print()

        response.raise_for_status()


        data = response.json()

        self.logger.info("LM Studio request completed.")

        if DEBUG:

            print()

            print("=" * 60)

            print("LM STUDIO RESPONSE")

            print(data)

            print("=" * 60)

            print()

        self.logger.info("LLM response parsed.")

        return data["choices"][0]["message"]["content"].strip()

    def classify_intent(self, request):

        return self._chat(

            INTENT_CLASSIFIER_PROMPT,

            request

        ).lower()

    def analyze_capability(self, goal):

        result = self._chat(

            CAPABILITY_ANALYZER_PROMPT,

            goal

        )

        #
        # Sometimes LLMs wrap JSON inside ```json
        #

        result = result.replace("```json", "")

        result = result.replace("```", "")

        result = result.strip()

        try:

            return json.loads(result)

        except Exception as e:

            self.logger.error(f"Capability JSON parsing failed: {e}")

            self.logger.error(result)

            return {

                "missing_capabilities": [],

                "suggested_skill": "UnknownSkill",

                "estimated_complexity": "Unknown",

                "dependencies": [],

                "permissions": []

            }

    def summarize(self, text):

        system_prompt = """
You are an engineering research assistant.

Analyze the provided research.

Your response MUST follow this format exactly.

Topic: <ONE SHORT TOPIC>

Summary:
<concise engineering summary>

Rules:
- Topic must contain only the main subject.
- Never leave Topic empty.
- Never omit Topic.
- Do not add any extra headings.
"""

        summary = self._chat(

            system_prompt,

            text[:4000]

        )

        return self.parser.parse_summary(summary)