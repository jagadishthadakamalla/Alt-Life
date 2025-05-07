import requests
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_URL = "https://jagadishtestopenai2025.openai.azure.com/openai/deployments/gpt-4o-mini_Test/chat/completions?api-version=2025-01-01-preview"

def generate_alt_life_story(prompt: str) -> str:
    full_prompt = (
            f"Tell a short, real-feeling story about someone who says: '{prompt}'. "
            "Keep it under 3-4 sentences. Make it feel raw, relatable, and meaningful — like something they post about on Instagram or talk about with a close friend."
            )

    headers = {
        "api-key": AZURE_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a thoughtful, concise storyteller. "
                    "Write emotionally resonant, grounded alternate life stories in under 250 words. "
                    "Be vivid but brief — 3 to 4 sentences max. "
                    "Avoid excessive detail, fantasy, or long explanations. "
                    "Focus on key turning points or emotions."
                )
            },
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.4,
        "top_p": 0.85,
        "max_tokens": 600
    }

    try:
        print("Calling Azure OpenAI API with prompt:", full_prompt)
        response = requests.post(AZURE_URL, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        print("Azure response:", result)

        return result["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print("Response content:", response.text)
        return "Sorry, there was an issue with the Azure API request."

    except Exception as err:
        print(f"Other error occurred: {err}")
        return "Sorry, an unexpected error occurred while generating the story."