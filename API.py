from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rasa.core.agent import Agent
import asyncio

app = FastAPI()

# Load the Rasa model
agent = Agent.load("20241117-150918-cyan-bandwidth.tar.gz")  # Replace with the path to your Rasa model file

# Define the request body
class MessageRequest(BaseModel):
    message: str

@app.post("/chatbot/")
async def chatbot_response(request: MessageRequest):
    try:
        responses = await agent.handle_text(request.message)
        # Extract the text of each response
        messages = [resp.get("text", "") for resp in responses if "text" in resp]
        return {"responses": messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling message: {str(e)}")

