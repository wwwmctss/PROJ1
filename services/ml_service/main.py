import os

from fastapi import FastAPI, Body
from api_handler import FastAPIHandler

app = FastAPI(title="Mobile Price Prediction Service")

handler = FastAPIHandler(
    model_path=os.getenv("MODEL_PATH", "../models/model.pkl")
)

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/api/prediction")
def prediction(item_id: int, body: dict = Body(...)):
    predict_value = handler.predict(body)
    return {"item_id": item_id, "predict": predict_value}