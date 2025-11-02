from pydantic import BaseModel, PositiveFloat

from typing import Literal

class BitcoinSchema(BaseModel):
    amount: PositiveFloat
    base: Literal['BTC']
    currency: Literal['USD']

    class Config:
        from_attributes = True