# 계산기 과제
1-1. 숫자부호(+,-,*,% ) 중 한가지와 두개의 숫자를 매개변수로 받아 부호에 해당하는 연산을 하는 함수를 만드세요
1-2. [1-1] 에서 만든 함수를 호출할 수 있는 api를 작성하세요

## 조건

a. 코드 작성시 패키지 구조를 분리하여 작성하시오.
    패키지 구조를 분리할때 구조를 분리한 이유를 readme파일에 작성하세요
b. 추가기능에 대한 설명도 readme 파일에 작성하세요

## 구조

fastAPI_practice/
│
├── main.py
├── calculator_crud.py
├── models.py
├── schemas.py
└── templates/
    └── calculator.html


## 기능

- 기본 +, -, * , / 연산 결과를 도출하고 기록이 남는 기능
- 전체 연산기록 조회(r)
- 전체 연산기록 삭제(d)로 인한 초기화 기능
