# [1. 파이썬 조건문의 기본 구조]

score = 85

# 자바와 달리 조건식에 괄호()를 쓰지 않음 (써도 되지만 안 쓰는 게 파이썬 스타일)
# 실행 블록은 중괄호{} 대신 콜론(:)과 '들여쓰기'로 구분함
if score >= 90:
	print("A학점임")
# 자바의 else if는 파이썬에서 elif로 줄여서 씀
elif score >= 80:
	print("B학점임")
elif score >= 70:
	print("C학점임")
else:
	print("F학점임")


# [2. 논리 연산자: &&, || 대신 영어로 씀]

is_java_hard = True
is_python_easy = True

# 자바의 && -> and
# 자바의 || -> or
# 자바의 !  -> not
if is_java_hard and is_python_easy:
	print("자바는 어렵지만 파이썬은 할 만하다는 뜻임")


# [3. 파이썬에만 있는 대박 편리한 비교]

money = 11000
# 자바에서는 (money >= 1000 && money <= 10000) 이렇게 길게 써야 함
# 파이썬은 수학 기호처럼 한 줄에 비교 가능함
if 1000 <= money <= 10000:
	print("예산 범위 안에 있음")
else:
	print("예상 범위 밖에 있음")