# 🐍 8일차 실습 확장: 실무 단골 내장 모듈 총정리

# 방식 1: 모듈 통째로 가져오기 (import 모듈명)
import random

# 모듈이름.함수명() 형태로 사용함
print(random.randint(1, 10))  # 1부터 10 사이의 랜덤 정수 출력

# 방식 2: 특정 함수만 쏙 골라서 가져오기 (from 모듈명 import 함수명)
from datetime import datetime

# 모듈 이름 없이 바로 함수명()으로 사용 가능함
print(datetime.now())  # 현재 날짜와 시간 출력


# ================================================================
# [추가] 실무에서 매일 쓰는 핵심 내장 모듈 & 단골 함수 정리
# ================================================================

# 1. random 모듈의 다른 단골 함수들
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))  # 리스트에서 아무거나 하나 쏙 뽑아줌 (샘플링)


# 2. time 모듈: 프로그램 제어 및 시간 측정 (import 통째로 하기)
import time
# time.sleep(2)  # 프로그램을 2초 동안 일시정지 (크롤링이나 API 호출 오버헤드 방지용)


# 3. json 모듈: 리액트랑 통신할 때 무조건 씀! (자바의 Jackson/Gson 라이브러리 역할)
import json
user_dict = {"name": "수빈", "job": "개발자"}

# 딕셔너리를 JSON 문자열로 바꾸기 (Serialization)
json_string = json.dumps(user_dict, ensure_ascii=False)
print(json_string)  # 결과: '{"name": "수빈", "job": "개발자"}'


# 4. os 모듈: 파일 경로 및 시스템 제어 (자바의 File 클래스 역할)
import os
print(os.getcwd())  # Current Working Directory: 현재 이 코드가 실행되는 폴더 경로 출력


# 5. math 모듈: 올림, 내림 등 수학 연산 (자바의 Math 클래스)
import math
print(math.ceil(2.3))   # 올림 -> 3
print(math.floor(2.7))  # 내림 -> 2