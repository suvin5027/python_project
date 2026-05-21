# [1. 숫자형: 정수(int)와 실수(float)]

# 동적 타이핑: 변수 선언 시 타입을 명시하지 않음. 대입되는 값에 따라 타입 결정됨
apple = 5      # 현재 int(정수)
price = 1.5    # 현재 float(실수)

# 자동 형변환: 정수와 실수를 연산하면 결과는 자동으로 실수(float)가 됨
# 자바처럼 (double) 명시적 형변환이 필요 없어 편리하지만, 타입 변화를 인지해야 함
total = apple * price

# f-string: 문자열 내부에 변수 값을 삽입할 때 사용함 (f"문자열 {변수}")
# 리액트의 템플릿 리터럴(``)과 유사한 방식임
print(f"사과 {apple}개의 가격은 {total}달러임.")


# [2. 문자열(str): 자바와 다른 특징]

# 명칭 차이: 자바의 String과 같으나, 파이썬에서는 str이라는 약칭을 사용함 (소문자 주의)
string_test = "사과"

# 멀티라인 문자열: 따옴표 세 개(''') 사용. 줄바꿈(\n) 없이 코드 작성 형태 그대로 출력됨
message = """
파이썬 2일차 학습 내용.
기본 자료형과 연산자 실습 중임.
"""

# 문자열 연산 주의사항:
# - 문자열 * 정수: 가능 (반복 출력)
# - 문자열 * 실수: 불가능 (TypeError 발생. "사과" * 1.5는 에러임)


# [3. 불리언(bool)과 객체의 정체]

# 명칭 차이: 자바의 Boolean과 같으나, 파이썬에서는 bool이라는 약칭을 사용함
# 값 표기: 반드시 첫 글자가 대문자(True, False)여야 함. 소문자는 에러임
is_java_hard = True

# type() 함수와 <class '...'>의 의미:
# - 파이썬은 모든 데이터가 클래스(Class)로 정의된 '객체(Object)'임
# - 자바의 기본형(Primitive Type) 개념이 없음 (모든 것이 레퍼런스 타입과 유사함)
# - 따라서 type() 확인 시 해당 데이터의 소속 클래스가 출력되는 것임
print(type(is_java_hard))  # <class 'bool'>
print(type(string_test))   # <class 'str'>
print(type(apple))         # <class 'int'>


# [4. 실행 시점 에러(Runtime Error)와 타입 힌트]

# 에러 발생 시점: 자바는 실행 전(컴파일)에 잡지만, 파이썬은 실행 중 해당 줄을 읽을 때 에러 발생
# 예: apple = "사과"; print(apple * 1.5) -> 실행 전엔 조용하다가 실행 시 터짐

# 해결책 1 - type() 활용:
# - 애매할 때마다 print(type(변수))를 찍어 정체를 확인하는 습관이 중요함 (디버깅 핵심)

# 해결책 2 - 타입 힌트(Type Hinting):
# - 변수명 뒤에 ': 타입'을 기재하여 의도하는 자료형을 명시함 (자바의 안정성 도입)
# - IDE(VS Code 등)에서 실수를 미리 경고해 줄 수 있음 (실무 강력 권장)
count: int = 10
user_name: str = "수빈"


# [5. 명시적 형변환 (Casting)]

# 자바의 Integer.parseInt()나 String.valueOf() 대신 간단한 함수 사용함
# int(), str(), float(), bool() 함수를 사용하여 서로 변환 가능함
num_to_str = str(10)  # 숫자 10을 문자열 "10"으로 변환
str_to_int = int("5") # 문자열 "5"를 숫자 5로 변환