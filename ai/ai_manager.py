import requests

from config.settings import LOCAL_LLM_HOST
from ai.prompts import INTENT_CLASSIFIER_PROMPT


class AIManager:

    def __init__(self):

        self.url = f"{LOCAL_LLM_HOST}/chat/completions"

        self.model = "deepseek-r1-0528-qwen3-8b"

    def classify_intent(self, request):

        response = requests.post(

            self.url,

            json={

                "model": self.model,

                "messages": [

                    {
                        "role": "system",
                        "content": INTENT_CLASSIFIER_PROMPT
                    },

                    {
                        "role": "user",
                        "content": request
                    }

                ],

                "temperature": 0

            }

        )

        if not response.ok:
            print("\n========== LM STUDIO ERROR ==========")
            print(response.status_code)
            print(response.text)
            print("=====================================\n")
            response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"].strip().lower()