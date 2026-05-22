# =============================================================================
# 제5장 - 예외 처리와 디버깅 (Exception Handling & Debugging) | 직접 채우기
# =============================================================================


# =============================================================================
# 연습 1. raise 문으로 예외 발생시키기
# =============================================================================

# 입력값이 조건에 맞지 않으면 raise로 예외를 발생시킵니다.
# except Exception as err로 잡아서 str(err)로 메시지를 출력합니다.
def box_print(symbol, width, height):
	if len(symbol) != 1:
		raise Exception("symbol 오류 메세지")
	elif width <= 2:
		raise Exception("width 오류 메시지")
	elif height <= 2:
		raise Exception("height 오류 메시지")
	else:
		print(symbol * width)
		for i in range(height - 2):
			print(symbol + (' ' * (width - 2)) + symbol)
		print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		box_print(sym, w, h)
	except Exception as err:
		print('예외 발생: ' + str(err))


# =============================================================================
# 연습 2. except Exception as err
# =============================================================================

# try 블록에서 open()이 성공하면 다음 줄로 넘어가고,
# 실패하면 except 블록으로 점프합니다.
# def safe_open(filename):
# 	try:
# 		open(filename)
# 		return "파일 열기 성공"
# 	except Exception as err:
# 		return str(err)

# print(safe_open("없는파일.txt"))
# print(safe_open("chapters/ch05/test.txt"))


# =============================================================================
# 연습 3. assert 문
# =============================================================================

# assert는 조건이 False이면 AssertionError를 발생시키고 프로그램을 즉시 멈춥니다.
# 버그를 찾기 위한 용도이므로 try/except로 잡지 않습니다.
# def divide(a, b):
# 	assert b != 0, "b는 0이면 안됩니다."
# 	return a / b

# print(divide(10, 2))
# divide(10, 0)


# =============================================================================
# 연습 4. logging 기본 설정
# =============================================================================

# basicConfig로 로그 수준과 형식을 설정하고,
# DEBUG / INFO / WARNING / ERROR / CRITICAL 5가지 수준으로 메시지를 출력합니다.
# import logging

# logging.basicConfig(
# 	level=logging.DEBUG,
# 	format='%(asctime)s - %(levelname)s - %(message)s'
# )

# logging.debug("디버그 메세지입니다.")
# logging.info("정보 메세지입니다.")
# logging.warning("경고 메세지입니다.")
# logging.error("에러 메세지입니다.")
# logging.critical("심각한 에러 메세지입니다.")


# =============================================================================
# 연습 5. logging으로 변수 추적
# =============================================================================

# logging.debug()로 반복마다 변수 값을 기록하여 흐름을 추적합니다.
# 연습 6의 logging.disable()을 활성화하면 로그 없이 완료 메시지만 출력됩니다.

# import logging
# logging.basicConfig(
# 	level=logging.DEBUG,
# 	format='%(asctime)s - %(levelname)s - %(message)s'
# )
# def count_down(n):
# 	for i in range(n, -1, -1):
# 		logging.debug(i)
# 	print("카운트 다운 완료")

# logging.disable(logging.CRITICAL)   # 연습 6: 이 줄을 활성화하면 로그가 전부 꺼집니다.

# count_down(5)


# =============================================================================
# 연습 6. logging 비활성화
# =============================================================================

# logging.disable(logging.CRITICAL) 한 줄로 모든 로그를 끕니다.
# 연습 5의 count_down() 위에 포함하여 함께 작성하였습니다.


# =============================================================================
# 연습 7. 종합 미니 프로그램 — 안전한 나눗셈 계산기
# =============================================================================

# logging, assert, try/except를 모두 조합한 종합 예제입니다.
# assert는 b=0일 때 프로그램을 즉시 멈추고, try/except는 그 외 예외를 처리합니다.

# import logging
# logging.basicConfig(
# 	level=logging.DEBUG,
# 	format='%(asctime)s - %(levelname)s - %(message)s'
# )

# def safe_calc(a, b):
# 	logging.debug('a=' + str(a) + ', b=' + str(b))
# 	assert b != 0, "b는 0이면 안됩니다."
# 	try:
# 		return a / b
# 	except Exception as err:
# 		return str(err)

# print(safe_calc(10, 2))
# print(safe_calc(9, 3))
# print(safe_calc(10, 0))   # → AssertionError
