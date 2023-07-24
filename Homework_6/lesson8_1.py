from pydantic import BaseModel, Field
from typing import List

class MarketModel(BaseModel):
    title: str = Field(max_length=128)
    descr: str = Field(max_length=4096)
    price: float = Field(max_digits=8, decimal_places=2)
    count: int = Field(gt=0)

