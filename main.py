from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    url: str
    question: str

@app.post("/api/wrapper")
def make_prediction(prediction_request: PredictionRequest):
    url = prediction_request.url
    question = prediction_request.question
    json_body = {"question": question}
    
    response = requests.post(url, json=json_body)
    
    if response.status_code == 200:
        return {"response":response.json()}
    else:
        return {"error": "Failed to make the prediction request."}