# =============================================================================
# 제3장 - 반복문 (Loops) | 개념 설명
# =============================================================================


# =============================================================================
# 1. while 루프
# =============================================================================

# while 루프는 조건이 True인 동안 계속 같은 코드 블록을 반복합니다.
# 구성 요소:
#   - while 키워드
#   - 조건 (True 또는 False로 평가되는 표현식)
#   - 콜론(:)
#   - 다음 줄부터 들여쓰기된 코드 블록

# if 문과 while 문의 차이:
#   if  → 조건이 True이면 블록을 한 번 실행합니다.
#   while → 조건이 True인 동안 블록을 계속 반복합니다.

# 예제: yourName.py
# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1
# → 'Hello, world.'가 5번 출력됩니다.
# → spam이 5가 되는 순간 조건이 False가 되어 루프가 끝납니다.

spam = 0
while spam < 5:
	print('Hello, world.')
	spam = spam + 1


# =============================================================================
# 2. break 문
# =============================================================================

# break 문은 루프를 즉시 탈출합니다.
# while True: 와 함께 사용하여 무한 루프를 만들고,
# 원하는 조건을 만족할 때 break로 빠져나옵니다.

# 예제: yourName2.py (break를 이용한 이름 입력 루프)
# while True:
#     print('Please type your name.')
#     name = input('> ')
#     if name == 'your name':
#         break
# print('Thank you!')
# → 'your name'을 입력하면 break로 루프를 탈출하고 'Thank you!'를 출력합니다.
# → 다른 값을 입력하면 계속 반복합니다.

# 무한 루프 주의:
# while True: 에서 break 없이 조건이 항상 True이면 프로그램이 끝나지 않습니다.
# 무한 루프에 빠지면 Ctrl+C로 강제 종료할 수 있습니다.


# =============================================================================
# 3. continue 문
# =============================================================================

# continue 문은 루프의 나머지 코드를 건너뛰고 루프의 처음으로 돌아갑니다.
# 루프를 완전히 끝내지 않고, 현재 반복만 건너뜁니다.

# break vs continue 비교:
#   break    → 루프 전체를 탈출합니다. (루프 종료)
#   continue → 현재 반복만 건너뛰고 다음 반복을 시작합니다. (루프 유지)

# 예제: swordfish.py (continue를 이용한 비밀번호 입력 루프)
# while True:
#     print('Who are you?')
#     name = input('> ')
#     if name != 'Joe':
#         continue       ← Joe가 아니면 이후 코드를 건너뛰고 처음으로 돌아갑니다.
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input('> ')
#     if password == 'swordfish':
#         break
# print('Access granted.')


# =============================================================================
# 4. Truthy 값과 Falsy 값
# =============================================================================

# 파이썬의 모든 값은 불리언 문맥에서 True 또는 False처럼 동작합니다.
# True처럼 동작하는 값을 Truthy, False처럼 동작하는 값을 Falsy라고 합니다.

# Falsy 값 (거짓처럼 동작하는 값):
#   0, 0.0, '' (빈 문자열)
# 나머지 값은 모두 Truthy입니다.

# bool() 함수로 값의 Truthy/Falsy 여부를 직접 확인할 수 있습니다.
print(bool(0))      # → False  (0은 Falsy입니다.)
print(bool(0.0))    # → False  (0.0은 Falsy입니다.)
print(bool(''))     # → False  (빈 문자열은 Falsy입니다.)
print(bool(42))     # → True   (0이 아닌 숫자는 Truthy입니다.)
print(bool('Hello'))   # → True   (비어 있지 않은 문자열은 Truthy입니다.)

# 활용 예시: while '' 은 조건이 False이므로 루프가 실행되지 않습니다.
# 반대로 while 'hello' 는 조건이 True이므로 무한 루프입니다.


# =============================================================================
# 5. for 루프와 range()
# =============================================================================

# for 루프는 range() 함수가 반환하는 값을 순서대로 변수에 담으며 반복합니다.
# 구성 요소:
#   - for 키워드
#   - 변수명 (각 반복에서 값을 받습니다.)
#   - in 키워드
#   - range() 함수 호출
#   - 콜론(:)
#   - 다음 줄부터 들여쓰기된 코드 블록

# 예제: fiveTimes.py
print('My name is')
for i in range(5):
	print('Jimmy Five Times (' + str(i) + ')')
# → i는 0, 1, 2, 3, 4 순서로 5번 반복됩니다.
# → range(5)는 0부터 4까지의 정수를 순서대로 반환합니다.

# for 루프로 1부터 100까지 합산하기 (가우스 합산):
total = 0
for num in range(101):
	total = total + num
print(total)   # → 5050


# =============================================================================
# 6. range() 함수의 인수
# =============================================================================

# range()는 1개, 2개, 또는 3개의 인수를 받을 수 있습니다.

# ── 인수 1개: range(stop) ─────────────────────────────────────────────────────
# 0부터 stop-1까지의 정수를 반환합니다.
# range(5) → 0, 1, 2, 3, 4
for i in range(5):
	print(i, end=' ')   # → 0 1 2 3 4
print()

# ── 인수 2개: range(start, stop) ──────────────────────────────────────────────
# start부터 stop-1까지의 정수를 반환합니다.
# range(12, 16) → 12, 13, 14, 15
for i in range(12, 16):
	print(i, end=' ')   # → 12 13 14 15
print()

# ── 인수 3개: range(start, stop, step) ────────────────────────────────────────
# start부터 stop-1까지 step 간격으로 정수를 반환합니다.
# step을 음수로 지정하면 역순으로 셀 수 있습니다.

# 예시: 0, 2, 4, 6, 8 (2 간격)
for i in range(0, 10, 2):
	print(i, end=' ')   # → 0 2 4 6 8
print()

# 예시: 5, 4, 3, 2, 1, 0 (역순 카운트다운)
for i in range(5, -1, -1):
	print(i, end=' ')   # → 5 4 3 2 1 0
print()

# 중요: range(10), range(0, 10), range(0, 10, 1) 은 모두 같은 결과를 반환합니다.
# (0부터 9까지 1씩 증가)


# =============================================================================
# 7. 모듈 임포트 (Importing Modules)
# =============================================================================

# 파이썬 표준 라이브러리의 모듈을 import 문으로 불러올 수 있습니다.
# 모듈은 관련 함수와 값의 집합입니다.

# 기본 import 방법:
import random
print(random.randint(1, 10))   # → 1~10 사이의 임의 정수를 반환합니다.

import sys
import os
import math

# 모듈 함수 호출 방법: 모듈이름.함수이름()
print(math.sqrt(16))   # → 4.0

# ── from ... import * ──────────────────────────────────────────────────────────
# from 모듈이름 import * 를 사용하면
# 모듈 이름 없이 함수를 바로 호출할 수 있습니다.

from random import *
print(randint(1, 10))   # → random. 없이 바로 호출합니다.

# 주의: from ... import * 는 어느 모듈에서 온 함수인지 알기 어려워집니다.
# 일반적으로 import 모듈이름 방식을 권장합니다.


# =============================================================================
# 8. sys.exit() — 프로그램 강제 종료
# =============================================================================

# sys.exit()를 호출하면 프로그램을 즉시 종료합니다.
# 프로그램 어느 위치에서든 호출할 수 있습니다.
# import sys 를 먼저 해야 사용할 수 있습니다.

# 예제: exitExample.py
# import sys
# while True:
#     print('Type exit to exit.')
#     response = input('> ')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')
# → 'exit'를 입력하면 sys.exit()가 호출되어 프로그램이 종료됩니다.

# 주의: 이 파일에서 sys.exit()를 실제로 실행하면 파일 전체 실행이 중단됩니다.
# 아래는 주석으로만 표시합니다.
# sys.exit()


# =============================================================================
# 9. 예제 프로그램 — guessTheNumber.py (숫자 맞추기)
# =============================================================================

# 1~20 사이의 숫자를 맞추는 게임입니다. 최대 6번 시도할 수 있습니다.

# # This is a guess the number game.
# import random
# secret_number = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
#
# # Ask the player to guess 6 times.
# for guesses_taken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input('>'))
#
#     if guess < secret_number:
#         print('Your guess is too low.')
#     elif guess > secret_number:
#         print('Your guess is too high.')
#     else:
#         break  # This condition is the correct guess!
#
# if guess == secret_number:
#     print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
# else:
#     print('Nope. The number was ' + str(secret_number))

# 핵심 포인트:
#   - range(1, 7)은 1, 2, 3, 4, 5, 6을 반환합니다. (6번 시도)
#   - 정답이면 else 블록에서 break로 for 루프를 탈출합니다.
#   - 루프 종료 후 for 루프 밖의 if-else로 성공/실패를 판별합니다.
#   - int(input('>')) : input()은 str을 반환하므로 int()로 변환합니다.


# =============================================================================
# 10. 예제 프로그램 — rpsGame.py (가위바위보)
# =============================================================================

# random과 sys 모듈을 함께 임포트합니다.
# wins, losses, ties 변수로 승/패/무 횟수를 추적합니다.
# while True(메인 루프) 안에 while True(입력 루프)가 중첩되어 있습니다.

# import random, sys
#
# print('ROCK, PAPER, SCISSORS')
#
# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0
#
# while True:  # The main game loop
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True:  # The player input loop
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         player_move = input('>')
#         if player_move == 'q':
#             sys.exit()  # Quit the program.
#         if player_move == 'r' or player_move == 'p' or player_move == 's':
#             break  # Break out of the player input loop.
#         print('Type one of r, p, s, or q.')
#
#     # Display what the player chose:
#     if player_move == 'r':
#         print('ROCK versus...')
#     elif player_move == 'p':
#         print('PAPER versus...')
#     elif player_move == 's':
#         print('SCISSORS versus...')
#
#     # Display what the computer chose:
#     move_number = random.randint(1, 3)
#     if move_number == 1:
#         computer_move = 'r'
#         print('ROCK')
#     elif move_number == 2:
#         computer_move = 'p'
#         print('PAPER')
#     elif move_number == 3:
#         computer_move = 's'
#         print('SCISSORS')
#
#     # Display and record the win/loss/tie:
#     if player_move == computer_move:
#         print('It is a tie!')
#         ties = ties + 1
#     elif player_move == 'r' and computer_move == 's':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'p' and computer_move == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 's' and computer_move == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'r' and computer_move == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif player_move == 'p' and computer_move == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif player_move == 's' and computer_move == 'r':
#         print('You lose!')
#         losses = losses + 1

# 핵심 포인트:
#   - while True 안에 while True를 중첩합니다. (루프 안의 루프)
#   - 안쪽 루프의 break는 안쪽 루프만 탈출합니다. 바깥 루프는 계속됩니다.
#   - sys.exit()는 루프와 관계없이 프로그램 자체를 종료합니다.
#   - '%s Wins, %s Losses, %s Ties' % (wins, losses, ties) 는
#     %s 자리에 순서대로 값을 채워 넣는 문자열 포맷팅입니다.
