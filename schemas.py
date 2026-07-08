from typing import Optional
from pydantic import baseModel

class passenger(baseModel):
    pclass:int
    sex:str

    age:Optional[float]=None
    fare:Optional[float]=None
