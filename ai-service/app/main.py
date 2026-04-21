from fastapi import FastAPI, HTTPException
from app.schemas import ReviewRequest
from app.ai.reviewer import generate_review
from app.utils.smart_chunker import smart_chunk
import json

app = FastAPI()

@app.get("/")
def home():
    print("Hi, I am home route :)")
    return {"status": "ok"}

@app.post("/review")
async def review_code(request: ReviewRequest):
    try:
        # use chunked files to prevent llm cost
        all_chunks = []

        for file in request.files:
            chunks = smart_chunk(file.path, file.content)
            all_chunks.extend(chunks)

        results = []
        for chunk in all_chunks:
            review = generate_review([chunk])
            results.append(review)

        # llm to json result
        try:
            res = json.loads(results)
        except:
            res = {
                "file": "",
                "line": -1,
                "review": results,
                "severity": "",
                "issues": [],
                "fix": []

            }
        return  res

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
