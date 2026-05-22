# =============================================================================
# 제5장 - 예외 처리와 디버깅 (Exception Handling & Debugging) | 개념 설명
# =============================================================================


# =============================================================================
# 1. raise 문 — 예외를 직접 발생시키기
# =============================================================================

# raise 문으로 Exception 객체를 직접 만들어 예외를 발생시킬 수 있습니다.
# 형식: raise Exception('에러 메시지')

# 예시 1: raise 기본 사용법
# raise Exception('이것은 에러 메시지입니다.')
# → Traceback (most recent call last):
#     ...
# Exception: 이것은 에러 메시지입니다.

# 예시 2: raise를 try/except로 잡기
def only_odd(number):
	if number % 2 == 0:
		raise Exception(str(number) + '은(는) 짝수입니다. 홀수만 입력하세요.')
	return number

try:
	result = only_odd(4)
except Exception as err:
	print('예외 발생:', str(err))   # → 예외 발생: 4은(는) 짝수입니다. 홀수만 입력하세요.


# =============================================================================
# 2. except Exception as err — 에러 메시지 꺼내기
# =============================================================================

# except Exception as err 로 예외 객체를 변수에 저장하고,
# str(err)로 에러 메시지를 문자열로 꺼낼 수 있습니다.

# 예시: boxPrint.py 핵심 구조
def box_print(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('symbol은 반드시 한 글자여야 합니다.')
	if width <= 2:
		raise Exception('width는 2보다 커야 합니다.')
	if height <= 2:
		raise Exception('height는 2보다 커야 합니다.')

	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		box_print(sym, w, h)
	except Exception as err:
		print('예외 발생: ' + str(err))   # str(err)로 에러 메시지를 꺼냅니다.


# =============================================================================
# 3. assert 문 — 검사 조건이 거짓이면 즉시 중단
# =============================================================================

# assert 조건, '메시지'
# → 조건이 True면 아무 일도 안 일어납니다.
# → 조건이 False면 AssertionError가 발생하고 프로그램이 멈춥니다.

# 형식
# assert 조건
# assert 조건, '에러 메시지'

# 예시 1: assert 기본
def calculate_speed(distance, time):
	assert time != 0, 'time은 0이면 안 됩니다.'
	return distance / time

# assert time != 0 → time이 0이면 AssertionError: time은 0이면 안 됩니다.

# 예시 2: 교통 신호 예제 (교재 예시)
market_2nd = {'ns': 'green', 'ew': 'red'}
# market_2nd['ns'] = 'green'
# market_2nd['ew'] = 'red'

def switch_lights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'
	# 남북과 동서가 동시에 초록불이 되면 안 된다는 불변 조건을 검사합니다.
	assert 'green' not in stoplight.values(), '동시에 초록불이 켜졌습니다!'

switch_lights(market_2nd)

# ★ assert vs try/except 차이
# - assert  : 프로그래머 실수(버그)를 잡는 용도입니다. try/except로 감싸지 않습니다.
# - try/except : 예상 가능한 사용자 입력 오류나 외부 환경 오류를 처리하는 용도입니다.
# - AssertionError를 try/except로 잡으면 assert의 의미가 사라집니다.


# =============================================================================
# 4. logging 모듈 — 디버깅용 로그 출력
# =============================================================================

# print() 대신 logging.debug()를 쓰면 나중에 한 번에 끄고 켤 수 있습니다.
# print()는 끄기 어렵지만, logging은 logging.disable()로 전체를 끌 수 있습니다.

import logging

# basicConfig — 로그 형식과 수준을 한 번 설정합니다.
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

# 로그 수준 (낮음 → 높음)
# DEBUG    : 가장 상세한 디버깅 정보
# INFO     : 일반 동작 확인
# WARNING  : 경고 (문제가 될 수 있는 상황)
# ERROR    : 오류 발생
# CRITICAL : 심각한 오류 (프로그램 중단 수준)

logging.debug('디버그 메시지입니다.')
logging.info('정보 메시지입니다.')
logging.warning('경고 메시지입니다.')
logging.error('에러 메시지입니다.')
logging.critical('심각한 에러 메시지입니다.')


# =============================================================================
# 5. logging 수준 — 어느 수준부터 출력할지 지정
# =============================================================================

# basicConfig(level=logging.DEBUG)   → DEBUG 이상 전부 출력
# basicConfig(level=logging.WARNING) → WARNING, ERROR, CRITICAL만 출력
# basicConfig(level=logging.ERROR)   → ERROR, CRITICAL만 출력

# 예시: 팩토리얼 함수에 로그 추가
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
	logging.debug('factorial(' + str(n) + ') 시작')
	total = 1
	for i in range(n + 1):
		total *= i
		logging.debug('i=' + str(i) + ', total=' + str(total))
	logging.debug('factorial(' + str(n) + ') 반환: ' + str(total))
	return total

# print(factorial(5))
# → 로그가 출력되면서 어느 줄에서 값이 바뀌는지 추적할 수 있습니다.


# =============================================================================
# 6. 로그 파일로 저장하기
# =============================================================================

# filename 인수를 추가하면 로그를 파일에 저장합니다.
# logging.basicConfig(
#     filename='myProgramLog.txt',
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# → 화면에는 출력되지 않고 파일에만 기록됩니다.


# =============================================================================
# 7. 로깅 비활성화
# =============================================================================

# 배포 시에는 로그를 전부 끄고 싶을 때 사용합니다.
# logging.disable(logging.CRITICAL) 한 줄로 모든 로그를 끕니다.

# logging.disable(logging.CRITICAL)   # → 이후 모든 logging 호출이 무시됩니다.
# logging.disable(logging.DEBUG)      # → DEBUG 이상(= 전부) 비활성화
# logging.disable(logging.WARNING)    # → WARNING 이상만 비활성화

# ★ 핵심: logging.disable(logging.CRITICAL)을 프로그램 상단 한 곳에 두면
# 나중에 주석 처리 한 번으로 전체 로그를 다시 활성화할 수 있습니다.
# print()는 하나하나 지워야 하므로 logging이 훨씬 편리합니다.


# =============================================================================
# 8. Mu 디버거 — 단계별 실행
# =============================================================================

# Mu 편집기의 Debug 모드에서 사용하는 버튼들입니다.

# [Continue]  → 다음 브레이크포인트까지 실행합니다.
# [Step Over] → 현재 줄을 실행하고 다음 줄로 이동합니다.
#               함수를 호출해도 함수 안으로 들어가지 않습니다.
# [Step In]   → 함수 안으로 들어가서 한 줄씩 실행합니다.
# [Step Out]  → 현재 함수를 끝까지 실행하고 호출한 곳으로 돌아갑니다.
# [Stop]      → 디버거를 종료합니다.

# 브레이크포인트 설정
# → 줄 번호 왼쪽을 클릭하면 빨간 점(●)이 생깁니다.
# → Debug 실행 시 해당 줄에서 자동으로 일시 정지합니다.
# → 변수 값을 확인하고 싶은 줄 직전에 설정합니다.

# ★ Step Over vs Step In 차이
# def greet():
#     print('안녕하세요!')   ← Step In 하면 여기로 들어옵니다.
#
# greet()  ← Step Over하면 이 줄을 통째로 실행하고 넘어갑니다.
#           ← Step In하면 greet() 함수 내부로 들어갑니다.


# =============================================================================
# 9. 종합 예제 — buggyAddingProgram.py 버그 수정
# =============================================================================

# 교재 예제: 세 숫자를 입력받아 합계를 출력하는 프로그램
# 버그: input()은 문자열을 반환하므로 + 연산이 숫자 덧셈이 아닌 문자열 연결이 됩니다.

# ❌ 버그 있는 코드
# print('세 숫자를 입력하세요.')
# first = input('첫 번째: ')
# second = input('두 번째: ')
# third = input('세 번째: ')
# print('합계: ' + first + second + third)   # → '123'처럼 연결됩니다.

# ✅ 수정한 코드
# print('세 숫자를 입력하세요.')
# first = int(input('첫 번째: '))
# second = int(input('두 번째: '))
# third = int(input('세 번째: '))
# print('합계: ' + str(first + second + third))   # → 숫자 덧셈이 됩니다.

# logging으로 디버깅하는 방법
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# ...
# logging.debug('first = ' + str(first))
# logging.debug('second = ' + str(second))
# logging.debug('third = ' + str(third))
# → 각 변수가 str인지 int인지 로그로 바로 확인할 수 있습니다.
