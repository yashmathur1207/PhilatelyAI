import json
import re
import os
import ollama
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
MODEL_NAME = 'gemma4:e4b'

SYSTEM_PROMPT = """You are an expert philatelist and stamp appraiser. 
Examine the uploaded stamp image carefully and provide a rigorous catalog entry.

Return your response in three clear sections:

### 🏷️ Catalog Summary
Provide a thorough visual breakdown covering:
- Primary Subject / Portrait
- Denomination / Face Value
- Inscriptions (transcribe visible text)
- Year / Issue Details
- Color Palette & Printing Type
- Cancellation / Condition

### 🛒 Marketplace Listing Draft
Write a compelling, SEO-optimized title and description suitable for eBay or Delcampe. Include suggested categories (e.g., Delcampe: Stamps > Asia > India).

### 📊 Philatelic Metadata (JSON)
Provide a strictly valid JSON block enclosed in ```json ``` with these keys:
{
  "country": "string",
  "subject": "string",
  "year": "string or number",
  "denomination": "string",
  "condition": "Mint / Used / Cancelled",
  "theme": "string",
  "inscriptions": ["list", "of", "detected", "text"]
}
"""

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/appraise")
async def appraise_stamp(image: UploadFile = File(...)):
    temp_path = f"temp_{image.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(await image.read())
    
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{
                'role': 'user',
                'content': SYSTEM_PROMPT,
                'images': [temp_path]
            }]
        )
        content = response['message']['content']

        json_match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL)
        json_str = json_match.group(1) if json_match else "{}"

        markdown_clean = re.sub(r'```json\s*.*?\s*```', '', content, flags=re.DOTALL).strip()

        return {"markdown": markdown_clean, "json": json_str}
    
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)