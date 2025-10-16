from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/olympus")
async def ask_olympus(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    return JSONResponse(content={
        "response": f"Olympus received your question: '{prompt}'. (This is a placeholder — you can customize this response.)"
    })
