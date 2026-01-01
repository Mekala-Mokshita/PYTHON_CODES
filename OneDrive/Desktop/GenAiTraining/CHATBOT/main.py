import os
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
from model import ChatRequest
from fastapi.middleware.cors import CORSMiddleware
#config .env
load_dotenv()
#getting apikey
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Gemini api key is empty")
#gemini api key config
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-flash-latest")

#important
app=FastAPI()
app.add_middleware(CORSMiddleware,allow_methods=["*"],allow_origins=["*"],allow_headers=["*"])
chat_session=model.start_chat(history=[])  #to save the previous records,responses and requests

@app.post("/chat")#127.0.0.1:8000/{"input token"}
async def chatbox(req:ChatRequest):
    try:
        response = chat_session.send_message (req.message) #stores in message 
        if not response:
            raise ValueError("Gemini gives empyt result")
        return {"reply":response.text}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))