# ============================================================
# 제8장 - 문자열 및 텍스트 편집
# 작성일: 2026/06/04
# ============================================================

# ────────────────────────────────────────────────────────────
# [1] 문자열 리터럴 (String Literals)
# ────────────────────────────────────────────────────────────

# 작은따옴표, 큰따옴표 모두 사용 가능합니다.
s1 = 'Hello'
s2 = "World"

# 큰따옴표 문자열 안에는 작은따옴표를 그냥 쓸 수 있습니다.
s3 = "That is Alice's cat."
print(s3)  # That is Alice's cat.

# ────────────────────────────────────────────────────────────
# [2] 탈출 시퀀스 (Escape Sequences)
# ────────────────────────────────────────────────────────────

# 특수 문자를 문자열 안에 넣을 때 백슬래시(\)를 앞에 붙입니다.
#   \'  → 작은따옴표
#   \"  → 큰따옴표
#   \t  → 탭
#   \n  → 줄바꿈 (newline)
#   \\  → 백슬래시 자체

print('Say hi to Bob\'s mother.')   # Bob's mother.
print("Hello there!\nHow are you?\nI'm doing fine.")
# Hello there!
# How are you?
# I'm doing fine.

print("파일 경로: C:\\Users\\Alice\\Desktop")  # \\ → \

# ────────────────────────────────────────────────────────────
# [3] 원시 문자열 (Raw Strings)
# ────────────────────────────────────────────────────────────

# r'' 접두사를 붙이면 백슬래시를 탈출 시퀀스로 해석하지 않습니다.
# 파일 경로나 정규 표현식을 쓸 때 유용합니다.

print(r'C:\Users\Alice\Desktop')    # C:\Users\Alice\Desktop (그대로 출력)
print('Hello...\n\n...world!')      # 줄바꿈 2번 발생
print(r'Hello...\n\n...world!')     # \n이 그대로 출력됨

# ────────────────────────────────────────────────────────────
# [4] 멀티라인 문자열 (Multiline Strings)
# ────────────────────────────────────────────────────────────

# 삼중 따옴표(''' 또는 """)로 여러 줄 문자열을 만들 수 있습니다.
# 줄바꿈, 탭, 따옴표를 그대로 포함할 수 있습니다.

letter = '''Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob'''

print(letter)

# 삼중 따옴표는 여러 줄 주석(docstring)으로도 활용합니다.
"""
이것은 여러 줄 주석입니다.
파이썬은 이 문자열을 실행하지 않습니다.
"""

# ────────────────────────────────────────────────────────────
# [5] 인덱스와 슬라이스 (Indexes and Slices)
# ────────────────────────────────────────────────────────────

# 문자열도 리스트처럼 인덱싱·슬라이싱할 수 있습니다.
# 6장의 리스트와 완전히 동일한 방식으로 동작합니다.

greeting = 'Hello, world!'
#            0123456789...
#           -13...........-1

print(greeting[0])      # H
print(greeting[4])      # o
print(greeting[-1])     # !  (마지막 문자)
print(greeting[0:5])    # Hello
print(greeting[:5])     # Hello  (처음부터 5 미만)
print(greeting[7:])     # world! (7부터 끝까지)
print(greeting[7:-1])   # world  (7부터 마지막 직전까지)

# 슬라이스는 원본을 바꾸지 않습니다.
greeting_slice = greeting[0:5]
print(greeting_slice)   # Hello
print(greeting)         # Hello, world!  (원본 그대로)

# ────────────────────────────────────────────────────────────
# [6] in / not in 연산자
# ────────────────────────────────────────────────────────────

# 문자열 안에 특정 문자열이 포함되어 있는지 확인합니다.
print('Hello' in 'Hello, World')    # True
print('HELLO' in 'Hello, World')    # False (대소문자 구분!)
print('cats' not in 'cats and dogs')  # False (들어있으므로)

# ────────────────────────────────────────────────────────────
# [7] f-string (포맷 문자열)
# ────────────────────────────────────────────────────────────

# f'' 접두사를 붙이고 {} 안에 변수나 표현식을 넣으면 자동으로 삽입됩니다.
# Python 3.6 이상에서 사용 가능합니다.

name = '박수빈'
age = 32
print(f'이름: {name}, 나이: {age}')             # 이름: 박수빈, 나이: 32
print(f'10년 후 나이: {age + 10}')              # 10년 후 나이: 42

# 중괄호 자체를 출력하려면 {{ }} (두 번 씁니다)
print(f'중괄호 출력: {{name}}')   # 중괄호 출력: {name}

# ────────────────────────────────────────────────────────────
# [7-1] f-string 이전 방식 (구버전 참고용)
# ────────────────────────────────────────────────────────────

# 방법 1: % 포맷 (Python 2 시절)
print('이름: %s, 나이: %s' % (name, age))

# 방법 2: format() 메서드
print('이름: {}, 나이: {}'.format(name, age))
print('{1}살, 이름은 {0}'.format(name, age))  # 인덱스로 순서 지정

# 현대 파이썬에서는 f-string이 가장 권장됩니다.

# ────────────────────────────────────────────────────────────
# [8] 문자열 메서드 - 대소문자 변환
# ────────────────────────────────────────────────────────────

# upper() / lower(): 대문자/소문자로 변환한 새 문자열을 반환합니다.
# 원본 문자열은 변하지 않습니다 (문자열은 불변!)
spam = 'Hello, world!'
print(spam.upper())     # HELLO, WORLD!
print(spam.lower())     # hello, world!
print(spam)             # Hello, world!  (원본 그대로)

# 변경하려면 재할당해야 합니다.
spam = spam.upper()
print(spam)             # HELLO, WORLD!

# isupper() / islower(): 모든 문자가 대문자/소문자인지 확인합니다.
print('HELLO'.isupper())        # True
print('Hello'.isupper())        # False
print('abc123'.islower())       # True  (숫자는 무관)
print('12345'.islower())        # False (문자가 하나도 없음)

# 메서드 체이닝: 메서드 결과에 또 다른 메서드를 이어서 호출할 수 있습니다.
print('Hello'.upper().lower())  # hello
print('HELLO'.lower().islower())  # True

# ────────────────────────────────────────────────────────────
# [9] 문자열 메서드 - isX() (문자열 특성 확인)
# ────────────────────────────────────────────────────────────

# isalpha()    : 문자(영문자)로만 구성 & 빈 문자열 아님
# isalnum()    : 문자 또는 숫자로만 구성 & 빈 문자열 아님
# isdecimal()  : 숫자로만 구성 & 빈 문자열 아님
# isspace()    : 공백(스페이스, 탭, 줄바꿈)으로만 구성 & 빈 문자열 아님
# istitle()    : 각 단어가 대문자로 시작하고 나머지는 소문자

print('hello'.isalpha())          # True
print('hello123'.isalpha())       # False (숫자 포함)
print('hello123'.isalnum())       # True
print('123'.isdecimal())          # True
print('   '.isspace())            # True
print('This Is Title'.istitle())  # True

# 사용자 입력 검증에 활용합니다.
# 예: 나이 입력 시 숫자만 허용
age_input = '42'
if age_input.isdecimal():
	print(f'나이: {age_input}')
else:
	print('숫자를 입력해주세요.')

# ────────────────────────────────────────────────────────────
# [10] 문자열 메서드 - startswith() / endswith()
# ────────────────────────────────────────────────────────────

# 문자열이 특정 문자열로 시작하거나 끝나는지 확인합니다.
print('Hello, world!'.startswith('Hello'))   # True
print('Hello, world!'.endswith('world!'))    # True
print('abc123'.startswith('abcdef'))         # False
print('abc123'.endswith('12'))               # False

# ────────────────────────────────────────────────────────────
# [11] 문자열 메서드 - join() / split()
# ────────────────────────────────────────────────────────────

# join(): 리스트의 문자열들을 하나로 합칩니다.
# 구분자.join(리스트) 형태로 사용합니다.
animals = ['cats', 'rats', 'bats']
print(', '.join(animals))    # cats, rats, bats
print(' '.join(animals))     # cats rats bats
print('ABC'.join(animals))   # catsABCratsABCbats

# split(): 문자열을 나눠서 리스트로 반환합니다.
# 기본은 공백(스페이스, 탭, 줄바꿈)을 기준으로 나눕니다.
sentence = 'My name is Simon'
print(sentence.split())          # ['My', 'name', 'is', 'Simon']
print(sentence.split('m'))       # ['My na', 'e is Si', 'on']

# 멀티라인 문자열을 줄 단위로 나눌 때 유용합니다.
multiline = '''첫 번째 줄
두 번째 줄
세 번째 줄'''
print(multiline.split('\n'))  # ['첫 번째 줄', '두 번째 줄', '세 번째 줄']

# ────────────────────────────────────────────────────────────
# [12] 문자열 메서드 - rjust() / ljust() / center()
# ────────────────────────────────────────────────────────────

# 문자열을 지정한 너비에 맞춰 정렬합니다.
# rjust(너비): 오른쪽 정렬 (왼쪽에 공백 추가)
# ljust(너비): 왼쪽 정렬 (오른쪽에 공백 추가)
# center(너비): 가운데 정렬

print('Hello'.rjust(10))     # '     Hello'
print('Hello'.ljust(10))     # 'Hello     '
print('Hello'.center(20))    # '       Hello        '

# 두 번째 인자로 채울 문자를 지정할 수 있습니다.
print('Hello'.rjust(20, '*'))    # '***************Hello'
print('Hello'.ljust(20, '-'))    # 'Hello---------------'
print('Hello'.center(20, '='))   # '=======Hello========'

# 표 형식으로 출력할 때 유용합니다.
def print_table(data):
	print('이름'.ljust(10) + '점수'.rjust(5))
	print('-' * 15)
	for name, score in data:
		print(name.ljust(10) + str(score).rjust(5))

scores = [('Alice', 95), ('Bob', 87), ('Charlie', 100)]
print_table(scores)

# ────────────────────────────────────────────────────────────
# [13] 문자열 메서드 - strip() / lstrip() / rstrip()
# ────────────────────────────────────────────────────────────

# 문자열 양끝의 공백(또는 지정 문자)을 제거합니다.
# strip()  : 양쪽 공백 제거
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거

spam = '    Hello, World    '
print(spam.strip())     # 'Hello, World'
print(spam.lstrip())    # 'Hello, World    '
print(spam.rstrip())    # '    Hello, World'

# 인자로 제거할 문자들을 지정할 수 있습니다 (순서 무관).
spam2 = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam2.strip('ampS'))   # 'BaconSpamEggs'
# 'a', 'm', 'p', 'S' 문자들을 양끝에서 제거합니다.

# ────────────────────────────────────────────────────────────
# [14] 유니코드 코드 포인트 - ord() / chr()
# ────────────────────────────────────────────────────────────

# 모든 문자는 숫자(유니코드 코드 포인트)로 저장됩니다.
# ord(문자)  : 문자 → 코드 포인트 숫자
# chr(숫자)  : 코드 포인트 숫자 → 문자

print(ord('A'))    # 65
print(ord('a'))    # 97
print(ord('!'))    # 33
print(chr(65))     # 'A'
print(chr(97))     # 'a'

# 문자를 수학적으로 비교하거나 순서대로 처리할 때 활용합니다.
print(ord('A') < ord('B'))   # True  (A=65, B=66)
print(chr(ord('A') + 1))     # 'B'  (A+1 → B)

# ────────────────────────────────────────────────────────────
# [15] 클립보드 복사/붙여넣기 - pyperclip 모듈
# ────────────────────────────────────────────────────────────

# pyperclip 모듈로 클립보드에 텍스트를 복사하거나 가져올 수 있습니다.
# 설치: pip install pyperclip

# import pyperclip
# pyperclip.copy('Hello, world!')   # 클립보드에 복사
# text = pyperclip.paste()          # 클립보드에서 가져오기
# print(text)                       # Hello, world!

# 실제 사용 예 - 클립보드 텍스트에 글머리 기호(*) 추가:
# import pyperclip
# text = pyperclip.paste()
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i]
# text = '\n'.join(lines)
# pyperclip.copy(text)

print('pyperclip은 pip install pyperclip 으로 설치 후 사용합니다.')
