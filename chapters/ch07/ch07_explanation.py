# 제7장 - 사전과 데이터 구조화 (Dictionaries and Data Structures)
# 교재: 파이썬으로 지루한 작업을 자동화하기 3판

# ============================================================
# 1. 딕셔너리란?
# ============================================================
# 딕셔너리(dictionary)는 키(key)-값(value) 쌍으로 이루어진 자료구조입니다.
# 중괄호 {}를 사용하고, 콜론(:)으로 키와 값을 연결합니다.
# 리스트처럼 여러 값을 담지만, 인덱스(0, 1, 2...) 대신 키로 접근합니다.

my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}

print(my_cat['size'])   # 'fat'
print(my_cat['color'])  # 'gray'
print(my_cat['age'])    # 17

# 키는 문자열뿐만 아니라 정수도 사용 가능합니다.
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[42])     # 'The Answer'
print(spam[12345])  # 'Luggage Combination'

# 빈 딕셔너리입니다.
empty_dict = {}


# ============================================================
# 2. 딕셔너리 vs 리스트
# ============================================================
# 리스트는 순서가 있어 항목 순서가 다르면 다른 값입니다.
# 딕셔너리는 순서가 없어 키-값 쌍의 순서가 달라도 같은 값입니다.

list_a = ['cats', 'dogs', 'moose']
list_b = ['dogs', 'moose', 'cats']
print(list_a == list_b)  # False (순서가 다르면 다름)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham  = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  # True (순서 달라도 키-값이 같으면 같음)

# 없는 키에 접근하면 KeyError가 발생합니다.
# spam = {'name': 'Zophie'}
# spam['color']  # → KeyError: 'color'


# ============================================================
# 3. 값 추가 및 변경
# ============================================================
# 딕셔너리[키] = 값  으로 새 키-값을 추가하거나 기존 값을 변경합니다.

person = {'name': '수빈', 'age': 25}
person['job'] = '개발자'      # 새 키 추가입니다.
person['age'] = 26            # 기존 값 변경입니다.
print(person)  # {'name': '수빈', 'age': 26, 'job': '개발자'}

# del로 키-값 쌍을 삭제합니다.
del person['job']
print(person)  # {'name': '수빈', 'age': 26}


# ============================================================
# 4. keys(), values(), items() 메서드
# ============================================================
# 딕셔너리의 키, 값, 키-값 쌍을 순회할 때 사용합니다.

spam = {'color': 'red', 'age': 42}

# keys(): 키만 순회합니다.
for k in spam.keys():
	print(k)
# color
# age

# values(): 값만 순회합니다.
for v in spam.values():
	print(v)
# red
# 42

# items(): (키, 값) 튜플 쌍으로 순회합니다.
for item in spam.items():
	print(item)
# ('color', 'red')
# ('age', 42)

# 다중 할당 트릭과 함께 사용하면 키와 값을 따로 받을 수 있습니다.
for k, v in spam.items():
	print('키:', k, '/ 값:', v)

# in/not in으로 키 존재 여부를 확인합니다.
print('color' in spam)          # True
print('color' in spam.keys())   # True (동일한 의미)
print('red' in spam.values())   # True
print('age' not in spam.keys()) # False

# list()로 진짜 리스트로 변환할 수 있습니다.
print(list(spam.keys()))    # ['color', 'age']
print(list(spam.values()))  # ['red', 42]


# ============================================================
# 5. get() 메서드 — 안전한 값 접근
# ============================================================
# dict.get(키, 기본값) → 키가 없으면 KeyError 대신 기본값을 반환합니다.

picnic = {'apples': 5, 'cups': 2}

print(picnic.get('cups', 0))   # 2 (키가 있으면 그 값)
print(picnic.get('eggs', 0))   # 0 (키가 없으면 기본값)
print(picnic.get('eggs', '없음'))  # '없음'

# get() 없이 접근하면 KeyError가 발생합니다.
# print(picnic['eggs'])  # → KeyError!


# ============================================================
# 6. setdefault() 메서드 — 없을 때만 기본값 설정
# ============================================================
# dict.setdefault(키, 기본값)
# → 키가 없으면 기본값으로 설정하고 반환합니다.
# → 키가 이미 있으면 기존 값을 그대로 반환합니다. (변경 안 함)

spam = {'name': 'Pooka', 'age': 5}

spam.setdefault('color', 'black')  # 'color' 키가 없으니 'black'으로 설정됩니다.
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

spam.setdefault('color', 'white')  # 이미 'color'가 있으니 아무것도 안 합니다.
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'} (변경 없음)

# 활용 예: 문자열 내 각 글자 등장 횟수 세기
message = 'Hello, Python!'
count = {}
for char in message:
	count.setdefault(char, 0)  # 처음 등장하는 글자면 0으로 초기화합니다.
	count[char] += 1
print(count)


# ============================================================
# 7. in/not in 연산자 (딕셔너리에서)
# ============================================================
# 딕셔너리에서 in은 기본적으로 키를 검색합니다.

my_dict = {'a': 1, 'b': 2, 'c': 3}

print('a' in my_dict)           # True (키 검색)
print('a' in my_dict.keys())    # True (동일)
print(1 in my_dict.values())    # True (값 검색)
print('z' not in my_dict)       # True


# ============================================================
# 8. 중첩 딕셔너리와 리스트 (Nested Dictionaries & Lists)
# ============================================================
# 딕셔너리의 값으로 또 다른 딕셔너리나 리스트를 넣을 수 있습니다.
# 복잡한 현실 데이터를 구조화하는 데 매우 유용합니다.

# 예: 소풍 참여자별 가져오는 물품
all_guests = {
	'Alice': {'apples': 5, 'pretzels': 12},
	'Bob':   {'ham sandwiches': 3, 'apples': 2},
	'Carol': {'cups': 3, 'apple pies': 1},
}

# Alice가 가져오는 사과 개수
print(all_guests['Alice']['apples'])  # 5

# 전체 사과 합계를 구하는 함수입니다.
def total_brought(guests, item):
	num = 0
	for k, v in guests.items():
		num += v.get(item, 0)  # 해당 항목이 없으면 0으로 처리합니다.
	return num

print('사과 총합:', total_brought(all_guests, 'apples'))        # 7
print('컵 총합:',   total_brought(all_guests, 'cups'))          # 3
print('케이크 총합:', total_brought(all_guests, 'cakes'))       # 0


# ============================================================
# 9. 실용 예제 — 생일 데이터베이스
# ============================================================
# 딕셔너리를 활용해 이름-생일 데이터를 관리하는 예제입니다.

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

name = 'Alice'
if name in birthdays:
	print(birthdays[name] + '은 ' + name + '의 생일입니다.')
else:
	print(name + '의 생일 정보가 없습니다.')
