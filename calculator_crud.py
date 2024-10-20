from sqlalchemy.orm import Session
from models import Calculation

# 전체 연산 기록 조회
def get_calculations(db: Session):
    return db.query(Calculation).all()


# 연산 기록 초기화 (모두 삭제)
def delete_all_calculations(db: Session):
    db.query(Calculation).delete()
    db.commit()
