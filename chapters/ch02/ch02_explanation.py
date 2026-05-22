# =============================================================================
# 제2장 - 흐름 제어 (Flow Control) | 개념 설명
# =============================================================================


# =============================================================================
# 1. 불리언 값 (Boolean Values)
# =============================================================================

# 불리언(Boolean) 데이터 타입은 True와 False, 단 두 가지 값만 가집니다.
# 반드시 첫 글자를 대문자로 씁니다. 따옴표 없이 씁니다.

spam = True
print(spam)   # → True

# 주의 1: 소문자로 쓰면 에러가 발생합니다.
# true  → NameError: name 'true' is not defined

# 주의 2: True/False를 변수명으로 사용할 수 없습니다.
# False = 2 + 2  → SyntaxError: can't assign to False

# type()으로 확인하면 bool 타입임을 알 수 있습니다.
print(type(True))   # → <class 'bool'>


# =============================================================================
# 2. 비교 연산자 (Comparison Operators)
# =============================================================================

# 비교 연산자(관계 연산자)는 두 값을 비교하여 True 또는 False를 반환합니다.
#
# 표 2-1: 비교 연산자
# ┌──────┬──────────────────────────┐
# │  ==  │ 같다 (Equal to)          │
# │  !=  │ 같지 않다 (Not equal to) │
# │  <   │ 보다 작다 (Less than)    │
# │  >   │ 보다 크다 (Greater than) │
# │  <=  │ 작거나 같다              │
# │  >=  │ 크거나 같다              │
# └──────┴──────────────────────────┘

print(42 == 42)    # → True
print(42 == 99)    # → False
print(2 != 3)      # → True
print(2 != 2)      # → False

# == 와 != 는 모든 데이터 타입에서 사용할 수 있습니다.
print('hello' == 'hello')   # → True
print('hello' == 'Hello')   # → False  (대소문자를 구별합니다)
print('dog' != 'cat')       # → True
print(True == True)         # → True
print(True != False)        # → True
print(42 == 42.0)           # → True   (숫자 값이 같으면 타입이 달라도 같다고 평가됩니다)
print(42 == 42.2)           # → False  (42와 42.2는 값 자체가 다르므로 False입니다)
print(42 == '42')           # → False  (int와 str는 다릅니다)

# <, >, <=, >= 는 숫자(int, float)에서만 제대로 작동합니다.
eggs = 42
print(eggs <= 42)    # → True

my_age = 29
print(my_age >= 10)  # → True

# ──────────────────────────────────────────────────────────────────────────────
# 중요: == 와 = 의 차이
# ──────────────────────────────────────────────────────────────────────────────
# =  (할당 연산자): 오른쪽 값을 왼쪽 변수에 저장합니다.  예) spam = 5
# == (비교 연산자): 두 값이 같은지 비교합니다.           예) spam == 5
# ──────────────────────────────────────────────────────────────────────────────


# =============================================================================
# 3. 불리언 연산자 (Boolean Operators)
# =============================================================================

# and, or, not 세 가지입니다.
# 비교 연산자와 마찬가지로 True 또는 False로 평가됩니다.

# ── and (진리표 2-2) ──────────────────────────────────────────────────────────
# 양쪽이 모두 True일 때만 True를 반환합니다.
print(True and True)    # → True
print(True and False)   # → False
print(False and True)   # → False
print(False and False)  # → False

# ── or (진리표 2-3) ───────────────────────────────────────────────────────────
# or는 "둘 중 하나라도 True야?" 를 묻는 연산자입니다.
# 하나라도 True이면 True, 둘 다 False이면 False를 반환합니다.
#
# 주의: 일상 언어의 "또는"과 의미가 다릅니다.
# "False 또는 False" 를 "거짓이거나 거짓이다 → 맞는 말이잖아?" 로 읽으면 안 됩니다.
# 파이썬 or 는 값이 True인 것이 하나라도 있는지를 검사합니다.
# False or False → "첫 번째가 True야? 아니오. 두 번째가 True야? 아니오." → False
print(True or True)     # → True   (둘 다 True)
print(True or False)    # → True   (왼쪽이 True)
print(False or True)    # → True   (오른쪽이 True)
print(False or False)   # → False  (둘 다 True가 아니므로 False)

# ── not (진리표 2-4) ──────────────────────────────────────────────────────────
# 단항 연산자입니다. 불리언 값을 반전시킵니다.
print(not True)    # → False
print(not False)   # → True

# not을 여러 번 중첩할 수 있습니다 (실제로는 사용하지 않는 것이 좋습니다).
print(not not not not True)   # → True


# =============================================================================
# 4. 불리언 연산자와 비교 연산자 혼합 사용
# =============================================================================

# 비교 연산자는 불리언 값으로 평가되므로, 불리언 연산자와 함께 사용할 수 있습니다.

print((4 < 5) and (5 < 6))    # → True
print((4 < 5) and (9 < 6))    # → False
print((1 == 2) or (2 == 2))   # → True

# 평가 순서 예시: (4 < 5) and (5 < 6)
# → True and (5 < 6)
# → True and True
# → True

# 여러 연산자를 한 번에 사용할 수도 있습니다.
spam = 4
print(2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2)
# → True and not False and True
# → True and True and True
# → True

# 불리언 연산자 우선순위: not → and → or
# 수학 연산과 비교 연산이 모두 끝난 후 not, and, or 순서로 평가합니다.


# =============================================================================
# 5. 흐름 제어의 구성 요소 (Components of Flow Control)
# =============================================================================

# 흐름 제어문은 항상 '조건(condition)'으로 시작하고,
# '코드 블록(block of code)'이 뒤따릅니다.

# ── 조건 (Conditions) ─────────────────────────────────────────────────────────
# 조건이란 True 또는 False로 평가되는 표현식입니다.
# 지금까지 본 불리언 표현식이 곧 조건입니다.
# if, while 등의 흐름 제어 구문에서 어떤 코드를 실행할지 결정하는 데 사용합니다.

# ── 코드 블록 (Blocks of Code) ───────────────────────────────────────────────
# 들여쓰기로 묶인 코드 줄의 집합입니다.
# 블록에는 4가지 규칙이 있습니다:
#   1. 들여쓰기가 증가하면 새 블록이 시작됩니다.
#   2. 블록은 다른 블록을 포함할 수 있습니다.
#   3. 들여쓰기가 0 또는 바깥 블록 수준으로 줄어들면 블록이 끝납니다.
#   4. 콜론(:)으로 끝나는 문장 바로 다음에 새 블록이 시작됩니다.

# 예시 (username/password 코드에서 블록 식별):
# username = 'Mary'
# password = 'swordfish'
# if username == 'Mary':
#     print('Hello, Mary')          ← 블록 1 시작
#     if password == 'swordfish':
#         print('Access granted.')  ← 블록 2 (블록 1 안의 블록)
#     else:
#         print('Wrong password.')  ← 블록 3

# ── 프로그램 실행 (Program Execution) ────────────────────────────────────────
# 파이썬은 위에서 아래로 한 줄씩 코드를 실행합니다.
# 흐름 제어문을 사용하면 특정 조건에 따라 다른 줄로 이동합니다.


# =============================================================================
# 6. if 문
# =============================================================================

# 조건이 True일 때만 해당 블록의 코드를 실행합니다.
# 구성 요소:
#   - if 키워드
#   - 조건 (True 또는 False로 평가되는 표현식)
#   - 콜론(:)
#   - 다음 줄부터 들여쓰기된 코드 블록 (if 절)

name = 'Alice'
if name == 'Alice':
	print('Hi, Alice.')   # 조건이 True이므로 실행됩니다.

# name을 다른 값으로 바꾸면 이 줄은 건너뜁니다.


# =============================================================================
# 7. else 문
# =============================================================================

# if 조건이 False일 때 실행할 코드를 else 블록에 작성합니다.
# else 문에는 별도의 조건이 없습니다.
# 구성 요소:
#   - else 키워드
#   - 콜론(:)
#   - 다음 줄부터 들여쓰기된 코드 블록 (else 절)

name = 'Alice'
if name == 'Alice':
	print('Hi, Alice.')
else:
	print('Hello, stranger.')   # name이 'Alice'가 아니면 실행됩니다.


# =============================================================================
# 8. elif 문
# =============================================================================

# 여러 조건을 순서대로 검사할 때 사용합니다.
# if → elif → elif → ... → else 순으로 위에서부터 검사합니다.
# 처음으로 True인 블록 하나만 실행하고 나머지는 자동으로 건너뜁니다.
# 구성 요소:
#   - elif 키워드
#   - 조건
#   - 콜론(:)
#   - 다음 줄부터 들여쓰기된 코드 블록 (elif 절)

# 예제: vampire.py
name = 'Carol'
age = 3000
if name == 'Alice':
	print('Hi, Alice.')
elif age < 12:
	print('You are not Alice, kiddo.')
elif age > 2000:
	print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
	print('You are not Alice, grannie.')
# name='Carol', age=3000 → 두 번째 elif (age > 2000)가 True이므로
# "Unlike you, Alice is not an undead, immortal vampire."가 출력됩니다.

# ── elif 순서가 중요합니다! ────────────────────────────────────────────────────
# 아래는 순서를 바꿔서 버그가 생기는 예시입니다 (vampire2.py).
name = 'Carol'
age = 3000
if name == 'Alice':
	print('Hi, Alice.')
elif age < 12:
	print('You are not Alice, kiddo.')
elif age > 100:                             # ← age > 2000보다 앞에 있습니다.
	print('You are not Alice, grannie.')    # ← 3000 > 100이 True이므로 여기서 멈춥니다.
elif age > 2000:
	print('Unlike you, Alice is not an undead, immortal vampire.')   # ← 도달 불가
# 출력: "You are not Alice, grannie." (의도한 결과가 아닙니다!)

# ── if / elif / else 조합 (littleKid.py) ────────────────────────────────────
# else를 마지막에 붙이면 모든 조건이 False일 때 반드시 실행됩니다.
name = 'Carol'
age = 3000
if name == 'Alice':
	print('Hi, Alice.')
elif age < 12:
	print('You are not Alice, kiddo.')
else:
	print('You are neither Alice nor a little kid.')
# 출력: "You are neither Alice nor a little kid."


# =============================================================================
# 9. 예제 프로그램 — oppositeday.py (반대의 날)
# =============================================================================

# 오늘이 "반대의 날"이면 항상 반대로 대답하는 프로그램입니다.
# 이 프로그램은 항상 'Today is not Opposite Day.'를 출력합니다.

today_is_opposite_day = True

# today_is_opposite_day를 기반으로 say_it_is_opposite_day를 설정합니다.
if today_is_opposite_day == True:
	say_it_is_opposite_day = True
else:
	say_it_is_opposite_day = False

# 반대의 날이면 say_it_is_opposite_day를 토글합니다.
if today_is_opposite_day == True:
	say_it_is_opposite_day = not say_it_is_opposite_day

# 오늘이 어떤 날인지 출력합니다.
if say_it_is_opposite_day == True:
	print('Today is Opposite Day.')
else:
	print('Today is not Opposite Day.')
# today_is_opposite_day가 True든 False든 항상 'Today is not Opposite Day.'가 출력됩니다.
# → not 연산자로 한 번 뒤집히기 때문입니다.


# =============================================================================
# 10. 예제 프로그램 — dishonestcapacity.py (정직하지 않은 용량 계산기)
# =============================================================================

# 하드 드라이브 제조사는 TB/GB를 다르게 정의하여 실제 용량보다 크게 광고합니다.
# 이 프로그램은 실제 용량이 얼마인지 계산합니다.

print('Enter TB or GB for the advertised unit:')
unit = input('> ')

# 단위에 따라 실제 비율(discrepancy)을 계산합니다.
if unit == 'TB' or unit == 'tb':
	discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
	discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('> ')
advertised_capacity = float(advertised_capacity)

# 실제 용량을 계산하고, 소수점 둘째 자리로 반올림한 후 문자열로 변환합니다.
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)

# 핵심 계산 과정 (예: 10TB 입력 시):
# advertised_capacity * discrepancy  →  10 * 0.9094947017729282  →  9.094947017729282
# round(9.094947017729282, 2)        →  9.09
# str(9.09)                          →  '9.09'
# 'The actual capacity is ' + '9.09' + ' ' + 'TB'  →  출력

# 주의: TB 또는 GB 외의 값을 입력하면 discrepancy 변수가 정의되지 않아
# NameError: name 'discrepancy' is not defined 에러가 발생합니다.
