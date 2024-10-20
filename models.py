from sqlalchemy import Column, Integer, Float, String
from databases import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    num1 = Column(Float, nullable=False)
    num2 = Column(Float, nullable=False)
    operation = Column(String, nullable=False)
    result = Column(Float, nullable=False)
