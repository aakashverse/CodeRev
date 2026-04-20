from fastapi import FastAPI, HTTPException
from app.schemas import ReviewRequest
from app.ai.reviewer import generate_review
import json

app = FastAPI()

@app.get("/")
def home():
    print("Hi, I am home route :)")
    return {"status": "ok"}

@app.post("/review")
async def review_code(request: ReviewRequest):
    try:
        ai_response = await generate_review(request.files)

        # llm to json result
        try:
            res = json.loads(ai_response)
        except:
            res = {
                "file": "",
                "line": -1,
                "review": ai_response,
                "severity": "",
                "issues": [],
                "fix": []

            }
        return  res

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
