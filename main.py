from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from databases import engine, get_db
import models
import schemas, calculator_crud

# 데이터베이스 모델을 생성합니다.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})

@app.post("/calculate", response_model=schemas.CalculationResponse)
async def calculate(request: schemas.CalculatorRequest, db: Session = Depends(get_db)):
    num1 = request.num1
    num2 = request.num2
    operation = request.operation.lower()

    # 계산 수행
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise HTTPException(status_code=400, detail="0으로 나눌 수 없음")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="지원되지 않는 연산입니다.")

    # 결과를 데이터베이스에 저장
    calculation = models.Calculation(num1=num1, num2=num2, operation=operation, result=result)
    db.add(calculation)
    db.commit()
    db.refresh(calculation)

    return calculation

@app.get("/calculations", response_model=list[schemas.CalculationResponse])
def read_calculations(db: Session = Depends(get_db)):
    calculations = calculator_crud.get_calculations(db)
    return calculations

@app.delete("/calculations", response_model=dict)
def delete_calculations(db: Session = Depends(get_db)):
    calculator_crud.delete_all_calculations(db)
    return {"message": "모든 연산 기록이 삭제되었습니다."}

