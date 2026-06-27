"""
AI Manager

Central interface to the local LLM.
"""

import requests

from config.settings import LOCAL_LLM_HOST
from config.settings import LOCAL_MODEL
from config.settings import DEBUG

from ai.prompts import INTENT_CLASSIFIER_PROMPT
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

        response.raise_for_status()

        data = response.json()

        self.logger.log("LM Studio request completed.")

        if DEBUG:

            print()

            print("=" * 50)

            print("LM STUDIO RESPONSE")

            print(data)

            print("=" * 50)

            print()

        self.logger.log("LLM response parsed.")

        return data["choices"][0]["message"]["content"].strip()

    def classify_intent(self, request):

        return self._chat(

            INTENT_CLASSIFIER_PROMPT,

            request

        ).lower()

    def summarize(self, text):

        system_prompt = """
You are an engineering research assistant.

Summarize the provided content.

Output:

A concise engineering summary.
"""

        summary = self._chat(

            system_prompt,

            text[:4000]

        )

        return self.parser.parse_summary(summary)