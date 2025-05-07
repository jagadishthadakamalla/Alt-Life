import httpx
import os
from dotenv import load_dotenv

# Explicitly provide path to .env file in the backend directory
#env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
#load_dotenv(dotenv_path=env_path)
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(GROQ_API_KEY)
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

async def generate_alt_life(prompt: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama2-70b-chat",
        "messages": [
            {
                "role": "user",
                "content": f"Imagine an alternate life based on: {prompt}. Tell it like a vivid story."
            }
        ],
        "temperature": 0.9
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload
            )
            response.raise_for_status()  # raises error for non-200
            data = response.json()
            return {"story": data["choices"][0]["message"]["content"]}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}