# 제9장 - 정규 표현식 실습
# 아래 TODO를 직접 채워서 완성해 보세요!

import re

# ============================================================
# 실습 1: re.compile()과 search(), group() 기본 사용법
# ============================================================
# 정규 표현식 4단계: import re → compile() → search() → group()

sentence = 'My number is 415-555-4242. Call me!'

# \d{3}-\d{3}-\d{4} 패턴으로 Pattern 객체를 만듭니다.
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# pattern.search()로 Match 객체를 얻습니다.
match = pattern.search(sentence)

# match.group()으로 매칭된 전화번호를 출력합니다.
print(match.group())
# 예상 출력: 415-555-4242


# ============================================================
# 실습 2: 그룹(group)으로 일부만 추출하기
# ============================================================
# 힌트: r'(\d{3})-(\d{3}-\d{4})' 처럼 괄호로 나누면
#       group(1)은 지역번호, group(2)는 나머지가 됩니다.

phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_re.search('Call me at 415-555-4242 tonight.')

# group(1)로 지역번호만 출력합니다.
print(mo.group(1))
# 예상 출력: 415

# group(2)로 나머지 번호를 출력합니다.
print(mo.group(2))
# 예상 출력: 555-4242

# group()로 전체 번호를 출력합니다.
print(mo.group())
# 예상 출력: 415-555-4242

# groups()로 다중 할당하여 두 변수에 저장합니다.
area_code, main_num = mo.groups()
print(area_code, main_num)
# 예상 출력: 415 555-4242


# ============================================================
# 실습 3: 파이프(|)로 여러 패턴 중 하나 매칭하기
# ============================================================
# 힌트: r'Bat(man|mobile|copter)' 처럼 작성합니다.

sentence2 = 'Batmobile lost a wheel'

# 'Batman', 'Batmobile', 'Batcopter' 중 하나를 찾는 패턴입니다.
hero_re = re.compile(r'Bat(man|mobile|copter)')
mo2 = hero_re.search(sentence2)
print(mo2.group())   # 예상 출력: Batmobile
print(mo2.group(1))  # 예상 출력: mobile


# ============================================================
# 실습 4: findall()로 모든 매칭 찾기
# ============================================================
text = 'Cell: 415-555-9999 Work: 212-555-0000 Home: 718-555-1234'

# 전화번호 패턴으로 findall()을 실행하여 모든 매칭을 가져옵니다.
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
numbers = phone_pattern.findall(text)
print(numbers)
# 예상 출력: ['415-555-9999', '212-555-0000', '718-555-1234']


# ============================================================
# 실습 5: 문자 클래스로 모음 찾기
# ============================================================
sentence3 = 'RoboCop eats BABY FOOD.'

# 모음(대소문자 모두)을 찾는 문자 클래스 패턴입니다.
vowel_re = re.compile(r'[aeiouAEIOU]')
print(vowel_re.findall(sentence3))
# 예상 출력: ['o', 'o', 'e', 'a', 'A', 'O', 'O']

# 모음이 아닌 것을 찾는 부정 문자 클래스 패턴입니다.
non_vowel_re = re.compile(r'[^aeiouAEIOU]')
print(non_vowel_re.findall(sentence3))
# 예상 출력: ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']


# ============================================================
# 실습 6: 수량자 사용하기 (?, {n})
# ============================================================

# 'Batman'과 'Batwoman' 둘 다 매칭되는 패턴입니다. (wo)? 는 선택적 그룹입니다.
bat_re = re.compile(r'Bat(wo)?man')
print(bat_re.search('The Adventures of Batman').group())    # 예상: Batman
print(bat_re.search('The Adventures of Batwoman').group())  # 예상: Batwoman

# 'HaHaHa'(정확히 3번)만 매칭되는 패턴입니다.
ha_re = re.compile(r'(Ha){3}')
print(ha_re.search('HaHaHa') is not None)  # 예상: True
print(ha_re.search('HaHa') is None)        # 예상: True

# 'Ha'가 3번~5번 반복되는 경우 모두 매칭되는 패턴입니다.
ha_range_re = re.compile(r'(Ha){3,5}')
print(ha_range_re.search('HaHaHa').group())      # 예상: HaHaHa
print(ha_range_re.search('HaHaHaHaHa').group())  # 예상: HaHaHaHaHa


# ============================================================
# 실습 7: 탐욕적 vs 비탐욕적 매칭 비교
# ============================================================
html = '<To serve man> for dinner.>'

# 탐욕적 패턴으로 가장 긴 매칭을 찾습니다.
greedy_re = re.compile(r'<.*>')
print('탐욕적:', greedy_re.search(html).group())
# 예상 출력: <To serve man> for dinner.>

# 비탐욕적 패턴으로 가장 짧은 매칭을 찾습니다.
lazy_re = re.compile(r'<.*?>')
print('비탐욕적:', lazy_re.search(html).group())
# 예상 출력: <To serve man>


# ============================================================
# 실습 8: 시작(^)과 끝($) 앵커
# ============================================================

# 문자열 전체가 숫자로만 이루어진 경우를 검사하는 패턴입니다.
whole_num_re = re.compile(r'^\d+$')
print(whole_num_re.search('1234567890') is not None)   # 예상: True
print(whole_num_re.search('123abc456') is None)        # 예상: True
print(whole_num_re.search('0') is not None)            # 예상: True


# ============================================================
# 실습 9: re.IGNORECASE로 대소문자 무시
# ============================================================
# 힌트: re.compile(패턴, re.I) 또는 re.compile(패턴, re.IGNORECASE)

sentences = ['I love Python!', 'PYTHON is great', 'python coding']

# 'python'을 대소문자 구분 없이 찾는 패턴입니다.
case_re = re.compile(r'python', re.I)
for s in sentences:
	mo = case_re.search(s)
	if mo:
		print(mo.group())
# 예상 출력:
# Python
# PYTHON
# python


# ============================================================
# 실습 10: sub()로 문자열 치환하기
# ============================================================
msg = 'Agent Alice contacted Agent Bob. Agent Carol replied.'

# 'Agent 이름' 형태를 'CENSORED'로 치환하는 패턴과 sub()입니다.
agent_re = re.compile(r'Agent \w+')
result = agent_re.sub('CENSORED', msg)
print(result)
# 예상 출력: CENSORED contacted CENSORED. CENSORED replied.


# ============================================================
# 실습 11: re.VERBOSE로 가독성 높은 패턴 작성하기
# ============================================================
# re.VERBOSE를 사용하면 패턴 안에 줄바꿈, 공백, 주석(#)을 쓸 수 있습니다.
# 삼중 따옴표(''')로 여러 줄에 걸쳐 패턴을 작성합니다.

# r'(\d{3})-(\d{3}-\d{4})' 패턴을 re.VERBOSE로 풀어서 작성합니다.
verbose_phone = re.compile(r'''
	(\d{3})        # 지역번호 3자리
	-              # 하이픈 구분자
	(\d{3}-\d{4})  # 나머지 번호 (3자리-4자리)
''', re.VERBOSE)

mo3 = verbose_phone.search('My number is 415-555-4242.')
if mo3:
	print(mo3.group())   # 예상 출력: 415-555-4242
	print(mo3.group(1))  # 예상 출력: 415
	print(mo3.group(2))  # 예상 출력: 555-4242


# ============================================================
# 실습 12: 도전 문제 - 이메일 주소 찾기
# ============================================================
# 이메일 형식: 사용자명@도메인.최상위도메인
# 예: hello@example.com, user.name+tag@mail.google.co.kr
#
# 사용자명: 영문자, 숫자, 점(.), 언더스코어(_), 퍼센트(%), 플러스(+), 하이픈(-) 가능
# 도메인: 영문자, 숫자, 하이픈(-), 점(.) 가능
# 최상위도메인: 2~4글자의 영문자

text2 = 'Contact us at hello@example.com or support@python-study.org for help.'

# 이메일 주소를 찾는 정규 표현식 패턴입니다.
email_re = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
emails = email_re.findall(text2)
print(emails)
# 예상 출력: ['hello@example.com', 'support@python-study.org']
