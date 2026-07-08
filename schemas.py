from typing import optional
from pydantic import baseModel

class passenger(baseModel):
    pclass:int
    sex:str

    age:optional[float]=None
    Fare:optional[float]=None
