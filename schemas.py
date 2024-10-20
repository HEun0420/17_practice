from pydantic import BaseModel

class CalculatorRequest(BaseModel):
    num1: float
    num2: float
    operation: str

class CalculationResponse(BaseModel):
    id: int
    num1: float
    num2: float
    operation: str
    result: float

    class Config:
        orm_mode = True
