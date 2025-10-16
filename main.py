from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/olympus")
async def interact_with_olympus(request: Request):
    body = await request.json()
    mode = body.get("mode", "unknown")
    return JSONResponse(content={
        "mode": mode,
        "response": f"Olympus is in {mode} mode. Ready to help."
    })
