# 제9장 - 정규 표현식을 이용한 텍스트 패턴 매칭
# 정규 표현식(Regular Expression, Regex)은 텍스트에서 특정 패턴을 찾는 강력한 도구입니다.
# Ctrl+F 검색보다 훨씬 유연하게 패턴을 지정할 수 있습니다.

import re

# ============================================================
# 1. 정규 표현식 없이 패턴 찾기 (비교용 예제)
# ============================================================
# 정규 표현식 없이 전화번호(415-555-4242)를 찾으려면 이렇게 많은 코드가 필요합니다.

def is_phone_number(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

print(is_phone_number('415-555-4242'))  # True
print(is_phone_number('Moshi moshi'))   # False

# 문장 안에서 전화번호 찾기 (정규 표현식 없이)
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	segment = message[i:i+12]
	if is_phone_number(segment):
		print('Found:', segment)
# 이렇게 복잡한데, 정규 표현식을 쓰면 훨씬 간단해집니다.

# ============================================================
# 2. re 모듈과 정규 표현식으로 패턴 찾기
# ============================================================
# 정규 표현식 사용 4단계:
#   1단계: re 모듈 임포트
#   2단계: re.compile()로 Pattern 객체 생성 (r'' 원시 문자열 사용 권장)
#   3단계: Pattern.search()로 Match 객체 얻기 (없으면 None 반환)
#   4단계: Match.group()으로 매칭된 문자열 얻기

# \d 는 숫자 0~9 하나를 의미합니다.
# {3} 은 앞의 패턴이 정확히 3번 반복됨을 의미합니다.
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
match = phone_pattern.search('My number is 415-555-4242.')
print(match.group())  # '415-555-4242'

# search()가 None을 반환하면 group() 호출 시 에러가 납니다.
# 따라서 실제 코드에서는 if match: 로 확인하는 것이 좋습니다.
if match:
	print('전화번호 발견:', match.group())

# ============================================================
# 3. 괄호로 그룹화 (Grouping with Parentheses)
# ============================================================
# 괄호 ()로 묶으면 그룹을 만들 수 있습니다.
#   group(1) → 첫 번째 괄호 그룹
#   group(2) → 두 번째 괄호 그룹
#   group(0) 또는 group() → 전체 매칭 문자열
#   groups() → 모든 그룹을 튜플로 반환

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')
print(mo.group(1))   # '415' (지역번호)
print(mo.group(2))   # '555-4242' (나머지)
print(mo.group(0))   # '415-555-4242' (전체)
print(mo.group())    # '415-555-4242' (전체, 0과 동일)
print(mo.groups())   # ('415', '555-4242') (튜플)

# 다중 할당 트릭: groups()의 결과를 여러 변수에 한 번에 할당합니다.
area_code, main_number = mo.groups()
print(area_code)    # '415'
print(main_number)  # '555-4242'

# ============================================================
# 4. 이스케이프 문자 (Escape Characters)
# ============================================================
# 정규 표현식에서 특수 의미를 가진 문자들 (패턴으로 쓸 수 없음):
#   . ^ $ * + ? { } [ ] \ | ( )
# 이 문자들을 패턴으로 찾으려면 앞에 백슬래시(\)를 붙여야 합니다.

# 예: '(415) 555-4242' 형태의 전화번호 찾기
paren_pattern = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = paren_pattern.search('My phone number is (415) 555-4242.')
print(mo2.group())  # '(415) 555-4242'

# ============================================================
# 5. 파이프(|)로 여러 패턴 중 하나 매칭
# ============================================================
# | 는 "둘 중 하나"를 의미합니다. search()는 첫 번째로 찾은 매칭을 반환합니다.

cat_dog = re.compile(r'Cat|Dog')
mo3 = cat_dog.search('I have a Cat and a Dog.')
print(mo3.group())  # 'Cat' (가장 먼저 나온 것)

# 공통 접두어가 있을 때 그룹과 함께 사용합니다.
bat_pattern = re.compile(r'Bat(man|mobile|copter|cave)')
mo4 = bat_pattern.search('Batmobile lost a wheel')
print(mo4.group())   # 'Batmobile' (전체)
print(mo4.group(1))  # 'mobile' (그룹 1)

# ============================================================
# 6. findall() - 모든 매칭 반환
# ============================================================
# search() → 첫 번째 매칭만 Match 객체로 반환
# findall() → 모든 매칭을 리스트로 반환

# 그룹이 없는 경우 → 문자열 리스트 반환
no_group = re.compile(r'\d{3}-\d{3}-\d{4}')
result = no_group.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)  # ['415-555-9999', '212-555-0000']

# 그룹이 있는 경우 → 튜플 리스트 반환 (각 튜플이 하나의 매칭)
with_group = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result2 = with_group.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result2)  # [('415', '555', '9999'), ('212', '555', '0000')]

# findall()은 겹치는 매칭은 하지 않습니다.
d3 = re.compile(r'\d{3}')
print(d3.findall('1234'))    # ['123'] → '234'는 이미 '123'에 포함된 영역과 겹침
print(d3.findall('123456'))  # ['123', '456']

# ============================================================
# 7. 한정자(Qualifier): 어떤 문자를 매칭할지
# ============================================================

# --- 문자 클래스 [abc] ---
# [abc]  → a, b, c 중 하나
# [a-z]  → a부터 z까지 (범위)
# [a-zA-Z0-9] → 모든 영문자와 숫자

vowel_re = re.compile(r'[aeiouAEIOU]')
print(vowel_re.findall('RoboCop eats BABY FOOD.'))
# ['o', 'o', 'e', 'a', 'A', 'O', 'O']

# --- 부정 문자 클래스 [^abc] ---
# ^ 를 [ ] 안 첫 번째에 쓰면 "해당 문자가 아닌 것"을 의미합니다.
consonant_re = re.compile(r'[^aeiouAEIOU]')
print(consonant_re.findall('RoboCop eats BABY FOOD.'))
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# --- 단축 문자 클래스 (Shorthand Character Classes) ---
# \d → [0-9]         숫자
# \D → [^0-9]        숫자가 아닌 것
# \w → [a-zA-Z0-9_]  문자(알파벳+숫자+언더스코어)
# \W → [^a-zA-Z0-9_] 문자가 아닌 것
# \s → 공백, 탭, 줄바꿈
# \S → 공백이 아닌 것

# 예: 숫자 뒤에 공백, 그 뒤에 단어가 오는 패턴
num_word = re.compile(r'\d+\s\w+')
print(num_word.findall('12 drummers, 11 pipers, 10 lords, 9 ladies'))
# ['12 drummers', '11 pipers', '10 lords', '9 ladies']

# --- 점(.) - 줄바꿈 제외 모든 문자 1개 ---
at_re = re.compile(r'.at')
print(at_re.findall('The cat in the hat sat on the flat mat.'))
# ['cat', 'hat', 'sat', 'lat', 'mat']
# 주의: 'flat'은 'lat'만 매칭됩니다 (.은 딱 1글자이므로)

# ============================================================
# 8. 수량자(Quantifier): 얼마나 많이 매칭할지
# ============================================================

# --- ? : 0번 또는 1번 (선택적) ---
bat_re2 = re.compile(r'Bat(wo)?man')
print(bat_re2.search('The Adventures of Batman').group())   # 'Batman'
print(bat_re2.search('The Adventures of Batwoman').group()) # 'Batwoman'

# --- * : 0번 이상 ---
spam_re = re.compile(r'Eggs(and spam)*')
print(spam_re.search('Eggs').group())                     # 'Eggs' (0번)
print(spam_re.search('Eggs and spam').group())            # 'Eggs and spam' (1번)
print(spam_re.search('Eggs and spam and spam').group())   # 'Eggs and spam and spam' (2번)

# --- + : 1번 이상 (*과 달리 반드시 1번은 있어야 함) ---
plus_re = re.compile(r'Eggs(and spam)+')
print(plus_re.search('Eggs') is None)            # True (매칭 안 됨)
print(plus_re.search('Eggs and spam').group())   # 'Eggs and spam'

# --- {n} : 정확히 n번 ---
ha_exact = re.compile(r'(Ha){3}')
print(ha_exact.search('HaHaHa').group())   # 'HaHaHa'
print(ha_exact.search('HaHa') is None)    # True (2번은 안 됨)

# --- {n,m} : n번 이상 m번 이하 ---
ha_range = re.compile(r'(Ha){3,5}')
print(ha_range.search('HaHaHa').group())       # 'HaHaHa' (3번)
print(ha_range.search('HaHaHaHaHa').group())   # 'HaHaHaHaHa' (5번, 탐욕적)

# --- {n,} : n번 이상 / {,m} : 0번 이상 m번 이하 ---
# {3,} → 3번 이상
# {,5} → 0번 이상 5번 이하

# ============================================================
# 9. 탐욕적(Greedy) vs 비탐욕적(Non-greedy/Lazy) 매칭
# ============================================================
# 기본은 탐욕적 - 가능한 가장 긴 문자열을 매칭합니다.
# 수량자 뒤에 ? 를 붙이면 비탐욕적 - 가능한 가장 짧은 문자열을 매칭합니다.

greedy = re.compile(r'(Ha){3,5}')
lazy = re.compile(r'(Ha){3,5}?')

print(greedy.search('HaHaHaHaHa').group())  # 'HaHaHaHaHa' (최대 5번)
print(lazy.search('HaHaHaHaHa').group())    # 'HaHaHa' (최소 3번)

# .* (탐욕적) vs .*? (비탐욕적)
text2 = '<To serve man> for dinner.>'
greedy_re2 = re.compile(r'<.*>')
lazy_re2 = re.compile(r'<.*?>')
print(greedy_re2.search(text2).group())  # '<To serve man> for dinner.>' (긴 것)
print(lazy_re2.search(text2).group())    # '<To serve man>' (짧은 것)

# ? 는 두 가지 의미가 있습니다:
#   1) 수량자로 쓰일 때: 0번 또는 1번 (선택적)
#   2) 다른 수량자 뒤에 쓰일 때: 비탐욕적 매칭으로 전환

# ============================================================
# 10. re.DOTALL: 줄바꿈 포함한 모든 문자 매칭
# ============================================================
# 기본적으로 . 은 줄바꿈(\n)을 제외합니다.
# re.DOTALL을 두 번째 인수로 전달하면 .이 줄바꿈도 포함합니다.

multiline = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
no_dotall = re.compile(r'.*')
with_dotall = re.compile(r'.*', re.DOTALL)

print(no_dotall.search(multiline).group())    # 'Serve the public trust.' (첫 줄만)
print(with_dotall.search(multiline).group())  # 전체 문자열 (줄바꿈 포함)

# ============================================================
# 11. 시작(^)과 끝($) 앵커
# ============================================================
# ^  → 문자열의 시작에서만 매칭
# $  → 문자열의 끝에서만 매칭
# ^$ → 전체 문자열이 패턴과 완전히 일치해야 함

starts_hello = re.compile(r'^Hello')
print(starts_hello.search('Hello, world!') is not None)      # True
print(starts_hello.search('He said "Hello."') is None)       # True (시작이 아님)

ends_num = re.compile(r'\d$')
print(ends_num.search('Your number is 42') is not None)      # True
print(ends_num.search('Your number is forty two') is None)   # True

whole_num = re.compile(r'^\d+$')
print(whole_num.search('1234567890') is not None)    # True (전체가 숫자)
print(whole_num.search('12345xyz67890') is None)     # True (중간에 문자)

# --- \b, \B : 단어 경계 ---
# \b → 단어의 시작 또는 끝 (경계)
# \B → 단어 경계가 아닌 곳 (단어 중간)

cat_boundary = re.compile(r'\bcat.*?\b')
print(cat_boundary.findall('The cat found a catapult catalog in the catacombs.'))
# ['cat', 'catapult', 'catalog', 'catacombs']

# ============================================================
# 12. 대소문자 무시: re.IGNORECASE (또는 re.I)
# ============================================================
robocop_re = re.compile(r'robocop', re.I)
print(robocop_re.search('RoboCop is part man.').group())       # 'RoboCop'
print(robocop_re.search('ROBOCOP protects the innocent.').group())  # 'ROBOCOP'
print(robocop_re.search('Have you seen robocop?').group())     # 'robocop'

# ============================================================
# 13. sub() 메서드: 문자열 치환
# ============================================================
# pattern.sub(교체할 문자열, 대상 문자열) → 치환된 새 문자열 반환

agent_re = re.compile(r'Agent \w+')
result = agent_re.sub('CENSORED', 'Agent Alice contacted Agent Bob.')
print(result)  # 'CENSORED contacted CENSORED.'

# 역참조(Back Reference): \1, \2 등으로 그룹 내용을 치환 문자열에 포함
# Agent (\w)\w* 에서 (\w)는 이름 첫 글자 그룹, \w*는 나머지
# r'\1****' 에서 \1은 그룹 1 (이름 첫 글자)을 의미합니다.
agent_re2 = re.compile(r'Agent (\w)\w*')
result2 = agent_re2.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
print(result2)  # 'A**** contacted B****.'

# ============================================================
# 14. re.VERBOSE: 상세 모드 (복잡한 정규 표현식 가독성 향상)
# ============================================================
# re.VERBOSE를 전달하면 정규 표현식 안에 공백과 주석을 쓸 수 있습니다.
# 줄 끝의 # 이후는 주석으로 무시됩니다.

phone_verbose = re.compile(r'''
	(\d{3}|\(\d{3}\))?  # 지역 코드 (선택적): 123 또는 (123) 형태
	(\s|-|\.)?           # 구분자 (선택적): 공백, 하이픈, 점
	\d{3}                # 앞 세 자리
	(\s|-|\.)            # 구분자
	\d{4}                # 뒤 네 자리
	(\s*(ext|x|ext\.)\s*\d{2,5})?  # 내선 번호 (선택적)
''', re.VERBOSE)

mo5 = phone_verbose.search('Call me at 415-555-4242.')
if mo5:
	print(mo5.group())  # '415-555-4242'

# ============================================================
# 15. 플래그 조합: | (비트 OR) 연산자로 여러 플래그 동시 사용
# ============================================================
# re.IGNORECASE | re.DOTALL | re.VERBOSE 처럼 조합 가능합니다.
combined = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# ============================================================
# 16. Humre: 사람이 읽기 쉬운 정규 표현식 모듈
# ============================================================
# pip install humre 로 설치합니다.
# Humre는 re 모듈을 대체하지 않고, re.compile()에 넘길 가독성 높은 패턴 문자열을 생성합니다.

# 주요 상수 (문자 클래스 단축표현):
#   DIGIT         → r'\d'
#   NONDIGIT      → r'\D'
#   WORD          → r'\w'
#   NONWORD       → r'\W'
#   WHITESPACE    → r'\s'
#   NONWHITESPACE → r'\S'
#   PERIOD        → r'\.'   (실제 점, 이스케이프됨)
#   ANY_SINGLE    → r'.'    (줄바꿈 제외 모든 문자)

# 주요 함수 (수량자 표현):
#   exactly(3, DIGIT)       → r'\d{3}'
#   group('A')              → r'(A)'
#   optional('A')           → r'A?'
#   either('A', 'B', 'C')   → r'A|B|C'
#   between(3, 5, 'A')      → r'A{3,5}'
#   at_least(3, 'A')        → r'A{3,}'
#   at_most(3, 'A')         → r'A{,3}'
#   chars('A-Z')            → r'[A-Z]'
#   nonchars('A-Z')         → r'[^A-Z]'
#   zero_or_more('A')       → r'A*'
#   one_or_more('A')        → r'A+'
#   starts_with('A')        → r'^A'
#   ends_with('A')          → r'A$'
#   optional_group('A')     → r'(A)?'
#   group_either('A','B')   → r'(A|B)'

# 사용 예시 (주석 처리: humre 미설치 시 에러 방지)
# from humre import *
# phone_regex = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
# # phone_regex → '\\d{3}-\\d{3}-\\d{4}'
# pattern = re.compile(phone_regex)
# print(pattern.search('My number is 415-555-4242.').group())  # '415-555-4242'

# humre.parse()로 기존 정규 표현식을 Humre 코드로 변환할 수도 있습니다.
# import humre
# print(humre.parse(r'\d{3}-\d{3}-\d{4}'))
# → "exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)"

# ============================================================
# 17. 정규 표현식 기호 총정리
# ============================================================
# ? → 앞 패턴이 0번 또는 1번
# * → 앞 패턴이 0번 이상
# + → 앞 패턴이 1번 이상
# {n}   → 정확히 n번
# {n,}  → n번 이상
# {,m}  → 0번 이상 m번 이하
# {n,m} → n번 이상 m번 이하
# {n,m}? 또는 *? 또는 +? → 비탐욕적(Lazy) 매칭
# ^spam → 문자열이 spam으로 시작
# spam$ → 문자열이 spam으로 끝
# .     → 줄바꿈 제외 모든 문자 1개
# \d, \w, \s → 숫자, 단어문자, 공백
# \D, \W, \S → 각각의 반대
# [abc] → a, b, c 중 하나
# [^abc] → a, b, c가 아닌 것
# (Hello) → 'Hello'를 하나의 그룹으로 묶음
# A|B|C  → A, B, C 중 하나
