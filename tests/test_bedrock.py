from ai.bedrock_client import BedrockClient


client = BedrockClient()

response = client.chat(

    "Reply with exactly: Bedrock Connected"

)

print()

print("=" * 60)

print(response)

print("=" * 60)