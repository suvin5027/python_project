# 함수 정의하기
def hello(name):
	return f"안녕, {name}! 오늘도 열공이야!"

# 함수 호출하고 결과 받기
message = hello("수빈")
print(message)



# ===================================================



# [1. 리턴(Return)이 있는 함수]
# - 함수가 계산한 결과를 '값'으로 돌려줌
# - 이 값은 변수에 저장해서 나중에 다른 연산에 쓸 수 있음
def add(a, b):
	return a + b

result = add(10, 20) # 30이라는 값을 result에 저장
print(result)		# 저장된 값을 출력


# [2. 리턴(Return)이 없는 함수]
# - 함수 안에서 특정 동작(예: print)만 수행하고 끝남
# - 변수에 담을 필요 없이 함수 이름만 불러서 사용함
def welcome(name):
	print(f"{name}님, 환영합니다!")

welcome("수빈")	  # 바로 "수빈님, 환영합니다!" 출력됨