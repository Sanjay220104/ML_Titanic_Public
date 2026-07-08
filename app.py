from fastapi import FASTAPI

from predictor import predict
from schemas import passenger
app=FastApi(
    title-"titanic survival API",
    version="1.0"
)
@app.get("/")
def home():

    return{
        "message":"titanic predictiom API is running."
    }
@app.post("/predict")
def predict_survival(pessenger:passenger):

    result=predict(passenger.model_dump())

    return result