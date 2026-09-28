import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

# Validate that the API key is present
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not found.")

# Initialize the OpenAI client pointing to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Request a completion using the free router model
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)

# Print the model's text response
print(response.choices[0].message.content)