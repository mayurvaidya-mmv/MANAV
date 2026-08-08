import os

from dotenv import load_dotenv

load_dotenv()

print("Bearer Token Present :", os.getenv("AWS_BEARER_TOKEN_BEDROCK") is not None)
print("Region              :", os.getenv("AWS_REGION"))
print("Model               :", os.getenv("BEDROCK_MODEL_ID"))