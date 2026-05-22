# =============================================================================
# 제4장 - 함수 (Functions) | 개념 설명
# =============================================================================


# =============================================================================
# 1. 함수 정의 (def 문)
# =============================================================================

# 함수는 프로그램 안에 있는 작은 프로그램과 같습니다.
# def 문으로 함수를 정의합니다.
# 구성 요소:
#   - def 키워드
#   - 함수 이름
#   - 괄호 () 와 콜론 :
#   - 들여쓰기된 코드 블록 (함수 본문)
#
# 함수 본문은 def 문이 실행될 때가 아니라, 함수가 호출될 때 실행됩니다.

# 예제: helloFunc.py
def hello():
	# Prints three greetings
	print('Good morning!')
	print('Good afternoon!')
	print('Good evening!')

hello()
hello()
print('ONE MORE TIME!')
hello()
# 출력: 'Good morning!' ~ 'Good evening!'이 세 번 출력됩니다.

# 함수를 사용하지 않으면 같은 코드를 반복해서 붙여넣어야 합니다.
# 함수를 사용하면 코드 중복을 없애고, 수정도 한 곳에서만 하면 됩니다.


# =============================================================================
# 2. 인수와 매개변수 (Arguments & Parameters)
# =============================================================================

# 매개변수(parameter): 함수 정의에서 괄호 안에 오는 변수입니다.
# 인수(argument): 함수 호출 시 전달하는 값입니다.
#
# 용어 정리:
#   - define (정의)  : def 문으로 함수를 만드는 것입니다.
#   - call (호출)    : 함수를 실행시키는 것입니다.
#   - pass (전달)    : 함수 호출 시 값을 넘겨주는 것입니다.
#   - argument (인수): 함수 호출 시 전달하는 값입니다.
#   - parameter (매개변수): 인수를 받는 함수 내부의 변수입니다.

# 예제: helloFunc2.py
def say_hello_to(name):
	# Prints three greetings to the name provided
	print('Good morning, ' + name)
	print('Good afternoon, ' + name)
	print('Good evening, ' + name)

say_hello_to('Alice')
say_hello_to('Bob')
# say_hello_to('Alice') 호출 시 'Alice'(인수)가 name(매개변수)에 저장됩니다.

# 주의: 매개변수에 저장된 값은 함수가 반환되면 사라집니다.
# say_hello_to('Bob') 실행 후 print(name) → NameError 발생합니다.


# =============================================================================
# 3. 반환값과 return 문 (Return Values & return Statement)
# =============================================================================

# 함수 호출은 하나의 값으로 평가됩니다. 이 값을 반환값(return value)이라 합니다.
# return 문으로 반환값을 지정합니다.
# 구성 요소:
#   - return 키워드
#   - 반환할 값 또는 표현식

# 예제: magic8Ball.py (매직 8볼 — 1~9에 따라 다른 문자열 반환)
import random

def get_answer(answer_number):
	# Returns a fortune answer based on what int answer_number is, 1 to 9
	if answer_number == 1:
		return 'It is certain'
	elif answer_number == 2:
		return 'It is decidedly so'
	elif answer_number == 3:
		return 'Yes'
	elif answer_number == 4:
		return 'Reply hazy try again'
	elif answer_number == 5:
		return 'Ask again later'
	elif answer_number == 6:
		return 'Concentrate and ask again'
	elif answer_number == 7:
		return 'My reply is no'
	elif answer_number == 8:
		return 'Outlook not so good'
	elif answer_number == 9:
		return 'Very doubtful'

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)

# 함수 호출을 표현식으로 사용하면 한 줄로 줄일 수 있습니다.
print(get_answer(random.randint(1, 9)))


# =============================================================================
# 4. None 값
# =============================================================================

# None 은 값이 없음을 나타내는 특별한 값입니다.
# None 의 데이터 타입은 NoneType 입니다.
# 반드시 첫 글자를 대문자로 씁니다. (True, False와 동일한 규칙)
# 다른 언어에서는 null, nil, undefined 라고 부르기도 합니다.

# ── print() vs return 핵심 차이 ───────────────────────────────────────────────
# print() : 화면에 글자를 보여주는 것입니다. (출력)
# return  : 함수가 호출한 곳으로 값을 돌려주는 것입니다. (반환)
# 이 둘은 완전히 다릅니다!

# return 이 있으면 → 변수에 값을 저장할 수 있습니다.
def with_return():
	return '반환값입니다.'

result = with_return()
print(result)   # → 반환값입니다.

# return 이 없으면 → 변수에 None 이 저장됩니다.
def no_return():
	print('화면 출력만 합니다.')   # 화면에는 보이지만 돌려주는 값이 없습니다.

result = no_return()   # 화면: '화면 출력만 합니다.' 출력됨
print(result)          # → None (돌려줄 값이 없으므로 None 이 저장됩니다.)

# print() 함수 자체도 반환값이 없으므로 None 을 반환합니다.
spam = print('Hello!')   # → 'Hello!' 출력 후 spam에 None이 저장됩니다.
print(None == spam)      # → True

# 정리:
# - 함수를 그냥 호출(hello())하면 화면 출력은 항상 됩니다.
# - 함수를 변수에 저장(result = hello())하려면 return 이 있어야 합니다.
# - return 이 없으면 변수에 None 이 저장됩니다.


# =============================================================================
# 5. 키워드 인수 (Named Parameters)
# =============================================================================

# 파이썬은 대부분의 인수를 위치(순서)로 구분합니다.
# 예) random.randint(1, 10) 과 random.randint(10, 1) 은 다릅니다.

# 키워드 인수(named parameter)는 이름으로 구분하는 인수입니다.
# 주로 선택적 인수(optional argument)를 제공할 때 사용합니다.

# ── print()의 end 매개변수 ────────────────────────────────────────────────────
# print()는 기본적으로 출력 끝에 줄바꿈(\n)을 추가합니다.
# end='' 로 지정하면 줄바꿈 없이 출력합니다.

print('Hello', end='')
print('World')   # → HelloWorld (같은 줄에 출력됩니다.)

# 예제: coinflip.py (동전 던지기 100번 결과를 한 줄에 출력)
for i in range(100):
	if random.randint(0, 1) == 0:
		print('H', end=' ')
	else:
		print('T', end=' ')
print()   # 마지막에 줄바꿈을 출력합니다.

# ── print()의 sep 매개변수 ────────────────────────────────────────────────────
# 여러 값을 print()에 전달하면 기본적으로 공백으로 구분합니다.
print('cats', 'dogs', 'mice')           # → cats dogs mice
print('cats', 'dogs', 'mice', sep=',')  # → cats,dogs,mice


# =============================================================================
# 6. 호출 스택 (Call Stack)
# =============================================================================

# 함수를 호출하면 파이썬은 호출한 위치(줄 번호)를 기억합니다.
# 함수가 반환되면 그 위치로 돌아가 코드를 계속 실행합니다.
# 이 정보를 관리하는 구조를 호출 스택(call stack)이라 합니다.
#
# 호출 스택은 스택(stack) 구조입니다.
# → 항목은 항상 맨 위에서만 추가되거나 제거됩니다.
# → 현재 실행 중인 함수가 항상 스택의 맨 위에 있습니다.
# → 함수가 반환되면 스택에서 제거되고, 이전 함수로 돌아갑니다.
#
# 프레임 객체(frame object): 함수 호출 시 호출 스택에 추가되는 객체입니다.
# 호출된 줄 번호를 저장하여 반환 후 어디로 돌아갈지 기억합니다.

# 예제: abcdCallStack.py
def a():
	print('a() starts')
	b()
	d()
	print('a() returns')

def b():
	print('b() starts')
	c()
	print('b() returns')

def c():
	print('c() starts')
	print('c() returns')

def d():
	print('d() starts')
	print('d() returns')

a()
# 출력 순서: a starts → b starts → c starts → c returns
#           → b returns → d starts → d returns → a returns


# =============================================================================
# 7. 지역 범위와 전역 범위 (Local & Global Scope)
# =============================================================================

# 지역 범위(local scope): 함수 내부에서만 존재하는 변수의 범위입니다.
# 전역 범위(global scope): 함수 외부에서 정의되어 어디서든 접근 가능한 범위입니다.
# 지역 변수(local variable): 지역 범위에 존재하는 변수입니다.
# 전역 변수(global variable): 전역 범위에 존재하는 변수입니다.
#
# 함수가 반환되면 해당 지역 범위가 사라지고, 지역 변수도 함께 삭제됩니다.

# ── 범위 규칙 4가지 ───────────────────────────────────────────────────────────
# 1. 전역 범위(함수 밖)는 지역 변수에 접근할 수 없습니다.
# 2. 한 함수의 지역 범위는 다른 함수의 지역 변수에 접근할 수 없습니다.
# 3. 지역 범위(함수 안)에서는 전역 변수에 접근할 수 있습니다.
# 4. 같은 이름의 변수라도 다른 범위에 있으면 서로 다른 변수입니다.

# 규칙 1 예시: 전역에서 지역 변수 접근 → NameError
# def spam():
#     eggs = 'sss'    ← eggs는 spam() 의 지역 변수입니다.
# spam()
# print(eggs)         ← NameError: name 'eggs' is not defined

# 규칙 3 예시: 함수 안에서 전역 변수 접근
def spam_global():
	print(eggs)   # 전역 변수 eggs에 접근합니다.

eggs = 'GLOBALGLOBAL'
spam_global()
print(eggs)   # → GLOBALGLOBAL

# 규칙 4 예시: 같은 이름, 다른 범위 (localGlobalSameName.py)
# def spam():
#     eggs = 'spam local'    ← spam()의 지역 변수
#     print(eggs)
#
# def bacon():
#     eggs = 'bacon local'   ← bacon()의 지역 변수 (spam()의 eggs와 다릅니다.)
#     print(eggs)
#     spam()
#     print(eggs)
#
# eggs = 'global'            ← 전역 변수
# bacon()
# print(eggs)
# → bacon local / spam local / bacon local / global 순으로 출력됩니다.

# ── UnboundLocalError ─────────────────────────────────────────────────────────
# 함수 안에 할당문(=)이 있으면 파이썬은 그 변수를 지역 변수로 취급합니다.
# 할당 전에 사용하면 UnboundLocalError가 발생합니다.
#
# def spam():
#     print(eggs)    ← ERROR! eggs를 지역 변수로 보지만 아직 할당 안 됐습니다.
#     eggs = 'spam local'
#
# eggs = 'global'
# spam()   → UnboundLocalError: local variable 'eggs' referenced before assignment


# =============================================================================
# 8. global 문
# =============================================================================

# 함수 안에서 전역 변수를 수정하려면 global 문을 사용합니다.
# global 변수명 을 함수 맨 위에 선언하면 해당 변수는 전역 변수로 취급됩니다.

# 예제: globalStatement.py
def spam_modify():
	global eggs
	eggs = 'spam'   # 전역 변수 eggs를 수정합니다.

eggs = 'global'
spam_modify()
print(eggs)   # → spam (전역 변수가 변경됩니다.)

# ── 범위 식별 규칙 4가지 ──────────────────────────────────────────────────────
# 1. 함수 밖에 있는 변수는 항상 전역 변수입니다.
# 2. global 문이 선언된 변수는 해당 함수에서 전역 변수입니다.
# 3. 그 외에 함수 안에서 할당(=)이 있으면 지역 변수입니다.
# 4. 함수 안에서 할당도, global 선언도 없으면 전역 변수입니다.


# =============================================================================
# 9. 예외 처리 (Exception Handling) — try / except
# =============================================================================

# 에러(예외, exception)가 발생하면 프로그램이 즉시 종료됩니다.
# try/except 문으로 예외를 처리하면 프로그램이 종료되지 않고 계속 실행됩니다.
#
# 구조:
#   try:
#       [에러가 발생할 수 있는 코드]
#   except 에러종류:
#       [에러 발생 시 실행할 코드]
#
# try 블록에서 에러가 발생하면 즉시 except 블록으로 이동합니다.
# except 블록 실행 후 프로그램은 정상적으로 계속 진행합니다.
# try 블록에서 에러가 없으면 except 블록은 건너뜁니다.
# except 블록 실행 후에는 try 블록으로 돌아가지 않습니다.

# 예제: zeroDivide.py (0으로 나누기 예외 처리)
def divide(divide_by):
	try:
		return 42 / divide_by
	except ZeroDivisionError:
		print('Error: Invalid argument.')

print(divide(2))    # → 21.0
print(divide(12))   # → 3.5
print(divide(0))    # → Error: Invalid argument. (None 반환)
print(divide(1))    # → 42.0


# =============================================================================
# 10. 예제 프로그램 — zigzag.py (지그재그 애니메이션)
# =============================================================================

# 별표(*)가 좌우로 왔다갔다하는 애니메이션입니다.
# time.sleep()으로 0.1초씩 멈추며 무한 반복합니다.
# Ctrl+C로 종료하면 KeyboardInterrupt 예외가 발생합니다.
# except KeyboardInterrupt: sys.exit() 로 깔끔하게 종료합니다.

# import time, sys
#
# indent = 0              # 들여쓰기 공백 수입니다.
# indent_increasing = True  # True면 증가, False면 감소합니다.
#
# try:
#     while True:  # The main program loop
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1)  # Pause for 1/10th of a second.
#
#         if indent_increasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indent_increasing = False
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indent_increasing = True
# except KeyboardInterrupt:
#     sys.exit()

# 핵심 포인트:
#   - ' ' * indent : 공백 문자를 indent 수만큼 반복합니다.
#   - end='' : print() 뒤에 줄바꿈 없이 바로 다음 print()와 이어집니다.
#   - indent == 20 이 되면 방향 전환, indent == 0 이 되면 다시 전환합니다.
#   - KeyboardInterrupt는 Ctrl+C를 누를 때 발생하는 예외입니다.


# =============================================================================
# 11. 예제 프로그램 — spike.py (스파이크 애니메이션)
# =============================================================================

# '-' 문자로 점점 길어졌다 짧아지는 스파이크 모양을 반복 출력합니다.
# '-' * (i * i) 로 지수적으로 길이가 변합니다.

# import time, sys
#
# try:
#     while True:  # The main program loop
#         # Draw lines with increasing length:
#         for i in range(1, 9):
#             print('-' * (i * i))
#             time.sleep(0.1)
#
#         # Draw lines with decreasing length:
#         for i in range(7, 1, -1):
#             print('-' * (i * i))
#             time.sleep(0.1)
# except KeyboardInterrupt:
#     sys.exit()

# 핵심 포인트:
#   - range(1, 9) : i = 1, 2, 3, 4, 5, 6, 7, 8
#     → '-' * (1*1)=1, (2*2)=4, (3*3)=9 ... (8*8)=64 개의 '-'를 출력합니다.
#   - range(7, 1, -1) : i = 7, 6, 5, 4, 3, 2
#     → 반대 방향으로 줄어듭니다.
