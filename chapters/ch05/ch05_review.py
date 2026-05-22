# =============================================================================
# 제5장 - 예외 처리와 디버깅 (Exception Handling & Debugging) | 실수 & 복습 정리
# =============================================================================


# =============================================================================
# 📌 복습 — 핵심 개념 정리
# =============================================================================

# 1. raise 문
#    → raise Exception('메시지') 로 예외를 직접 발생시킵니다.
#    → try/except로 잡지 않으면 프로그램이 중단됩니다.
#    → except Exception as err 로 잡고, str(err) 로 메시지를 꺼낼 수 있습니다.

# 2. except Exception as err
#    → 예외 객체를 err 변수에 저장합니다.
#    → str(err) 로 에러 메시지를 문자열로 변환합니다.
#    → 형식:
#      try:
#          ...
#      except Exception as err:
#          print('예외 발생: ' + str(err))

# 3. assert 문
#    → assert 조건, '메시지' 형식으로 사용합니다.
#    → 조건이 True면 아무 일도 없습니다.
#    → 조건이 False면 AssertionError가 발생하고 프로그램이 즉시 멈춥니다.
#    → 프로그래머 실수(버그)를 잡는 용도입니다. try/except로 감싸지 않습니다.
#    → 사용자 입력 오류에는 assert 대신 try/except를 사용합니다.

# 4. logging 모듈
#    → print() 대신 logging.debug() 등을 사용하면 나중에 한 번에 끄고 켤 수 있습니다.
#    → 설정: logging.basicConfig(level=logging.DEBUG, format='...')
#    → 5가지 수준 (낮음 → 높음): DEBUG / INFO / WARNING / ERROR / CRITICAL
#    → 파일로 저장: basicConfig(filename='로그파일.txt', ...)
#    → 전체 비활성화: logging.disable(logging.CRITICAL)

# 5. Mu 디버거
#    → [Continue]  : 다음 브레이크포인트까지 실행합니다.
#    → [Step Over] : 현재 줄을 실행하고 다음 줄로 이동합니다. 함수 내부로 들어가지 않습니다.
#    → [Step In]   : 함수 내부로 들어가서 한 줄씩 실행합니다.
#    → [Step Out]  : 현재 함수를 끝까지 실행하고 호출한 곳으로 돌아갑니다.
#    → 브레이크포인트: 줄 번호 클릭 → 빨간 점(●) → 해당 줄에서 자동 일시정지


# =============================================================================
# ❌ 실수 & ✅ 수정
# =============================================================================

# ---------------------------------------------------------------
# ❌ 실수 1 : width <= 2 대신 width < 2 를 써서 width=2가 허용됨
# ---------------------------------------------------------------

# 틀린 코드
# def box_print(symbol, width, height):
#     elif width < 2:         ← width=2는 통과됩니다.
#         raise Exception(...)

# 원인
# "2 이하"는 width <= 2 (0, 1, 2 모두 에러)입니다.
# width < 2 는 "2 미만"이므로 width=2가 조건에 걸리지 않아 통과됩니다.

# ✅ 올바른 코드
def box_print(symbol, width, height):
	if len(symbol) != 1:
		raise Exception("symbol 오류 메세지")
	elif width <= 2:    # "2 이하" = <= 2 입니다.
		raise Exception("width 오류 메시지")
	elif height <= 2:   # "2 이하" = <= 2 입니다.
		raise Exception("height 오류 메시지")
	else:
		print(symbol * width)
		for i in range(height - 2):
			print(symbol + (' ' * (width - 2)) + symbol)
		print(symbol * width)

# 핵심 규칙
# "이하" → <= (해당 값 포함)
# "미만" → <  (해당 값 제외)


# ---------------------------------------------------------------
# ❌ 실수 2 : logging.debug(a, b) 로 인수를 두 개 넘기면 TypeError 발생
# ---------------------------------------------------------------

# 틀린 코드
# def safe_calc(a, b):
#     logging.debug(a, b)   ← TypeError 발생합니다.

# 원인
# logging.debug()는 첫 번째 인수를 메시지 문자열로만 받습니다.
# logging.debug(a, b) 처럼 두 개를 넘기면
# 두 번째 인수를 % 포맷 인수로 해석하다가 TypeError가 발생합니다.

# ✅ 올바른 코드
# import logging
# def safe_calc(a, b):
#     logging.debug('a=' + str(a) + ', b=' + str(b))   # 문자열 하나로 만들어서 넘깁니다.

# 핵심 규칙
# logging.debug()에는 문자열 하나만 넘깁니다.
# 여러 변수를 찍고 싶으면 + str()로 이어 붙입니다.


# ---------------------------------------------------------------
# ❌ 실수 3 : except 블록에서 str(err)만 쓰고 return을 빠뜨림
# ---------------------------------------------------------------

# 틀린 코드
# def safe_calc(a, b):
#     ...
#     except Exception as err:
#         str(err)   ← 변환만 하고 반환하지 않아 None이 반환됩니다.

# 원인
# str(err) 만 쓰면 문자열로 변환은 되지만 함수 밖으로 나가지 않습니다.
# return 이 없으므로 None 이 반환됩니다.

# ✅ 올바른 코드
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def safe_calc(a, b):
	logging.debug('a=' + str(a) + ', b=' + str(b))
	assert b != 0, 'b는 0이면 안됩니다.'
	try:
		return a / b
	except Exception as err:
		return str(err)   # return을 반드시 붙입니다.

# 핵심 규칙
# except 블록에서 값을 돌려주려면 반드시 return str(err) 로 작성합니다.
