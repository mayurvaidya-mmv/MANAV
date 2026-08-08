"""
AWS Bedrock Client

Used for high-level reasoning tasks:
- Capability Analysis
- Skill Generation
- Validation
- Test Generation
"""

import os

import boto3

from dotenv import load_dotenv


load_dotenv()


class BedrockClient:

    def __init__(self):

        self.model_id = os.getenv("BEDROCK_MODEL_ID")

        self.client = boto3.client(

            "bedrock-runtime",

            region_name=os.getenv("AWS_REGION"),

            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),

            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")

        )

    def chat(self, prompt: str):

        response = self.client.converse(

            modelId=self.model_id,

            messages=[

                {
                    "role": "user",

                    "content": [

                        {
                            "text": prompt
                        }

                    ]
                }

            ]

        )

        return response["output"]["message"]["content"][0]["text"]