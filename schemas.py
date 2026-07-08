from typing import optimal
from pydantic import baseModel

class passenger(baseModel):
    pclass:int
    sex:str

    age:optional[float]=None
    Fare:optional[float]=None