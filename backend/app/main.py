from fastapi import FastAPI
from pydantic import BaseModel
from routes.alt_life import generate_alt_life_story  # Correct import statement
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(request: PromptRequest):
    try:
        story = generate_alt_life_story(request.prompt)
        return {"result": story}
    except Exception as e:
        return {"error": str(e)}