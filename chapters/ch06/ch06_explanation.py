# 제6장 - 리스트 (Lists)
# 교재: 파이썬으로 지루한 작업을 자동화하기 3판

# ============================================================
# 1. 리스트란?
# ============================================================
# 리스트(list)는 순서가 있는 여러 값의 묶음입니다.
# 대괄호 []로 감싸고, 각 항목은 쉼표로 구분합니다.

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = ['hello', 3.14, True, None, 42]  # 여러 타입 혼합도 가능합니다.
empty = []  # 빈 리스트입니다.

print(fruits)   # ['apple', 'banana', 'cherry']
print(numbers)  # [1, 2, 3, 4, 5]
print(mixed)    # ['hello', 3.14, True, None, 42]


# ============================================================
# 2. 인덱스 (Index)
# ============================================================
# 리스트의 각 항목에는 0부터 시작하는 번호(인덱스)가 있습니다.
# spam[0] → 첫 번째 항목

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0])   # 'cat'
print(spam[1])   # 'bat'
print(spam[3])   # 'elephant'

# 음수 인덱스: 뒤에서부터 셉니다.
print(spam[-1])  # 'elephant' (마지막)
print(spam[-2])  # 'rat' (뒤에서 두 번째)

# 중첩 리스트 인덱스
nested = [['cat', 'bat'], [10, 20, 30]]
print(nested[0])     # ['cat', 'bat']
print(nested[0][1])  # 'bat'
print(nested[1][2])  # 30


# ============================================================
# 3. 슬라이스 (Slice)
# ============================================================
# 슬라이스는 리스트에서 여러 항목을 잘라내 새 리스트를 만듭니다.
# spam[시작:끝] → 시작 인덱스부터 끝 인덱스 직전까지 가져옵니다.

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0:4])   # ['cat', 'bat', 'rat', 'elephant'] 전체
print(spam[1:3])   # ['bat', 'rat']
print(spam[0:-1])  # ['cat', 'bat', 'rat'] 마지막 제외

# 시작 또는 끝 생략 가능합니다.
print(spam[:2])    # ['cat', 'bat'] 처음부터 인덱스 2 직전까지
print(spam[1:])    # ['bat', 'rat', 'elephant'] 인덱스 1부터 끝까지
print(spam[:])     # ['cat', 'bat', 'rat', 'elephant'] 전체 복사


# ============================================================
# 4. len() 함수
# ============================================================
# len()은 리스트의 항목 개수를 반환합니다.

spam = ['cat', 'dog', 'moose']
print(len(spam))  # 3


# ============================================================
# 5. 값 변경 (Value Updates)
# ============================================================
# 인덱스를 사용해 리스트의 특정 값을 바꿀 수 있습니다.

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)   # ['cat', 'aardvark', 'rat', 'elephant']

spam[-1] = 12345
print(spam)   # ['cat', 'aardvark', 'rat', 12345]


# ============================================================
# 6. 리스트 연결(+)과 복제(*)
# ============================================================
# 문자열처럼 리스트도 + 와 * 연산자를 사용할 수 있습니다.

print([1, 2, 3] + ['A', 'B', 'C'])  # [1, 2, 3, 'A', 'B', 'C']
print(['X', 'Y'] * 3)               # ['X', 'Y', 'X', 'Y', 'X', 'Y']

spam = [1, 2, 3]
spam += ['A', 'B', 'C']  # spam = spam + ['A', 'B', 'C']와 동일합니다.
print(spam)  # [1, 2, 3, 'A', 'B', 'C']


# ============================================================
# 7. del 문 (항목 삭제)
# ============================================================
# del 문으로 특정 인덱스의 항목을 삭제합니다.
# 삭제 후 뒤 항목들이 앞으로 당겨집니다.

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]   # 인덱스 2('rat') 삭제
print(spam)   # ['cat', 'bat', 'elephant']

del spam[0]   # 인덱스 0('cat') 삭제
print(spam)   # ['bat', 'elephant']


# ============================================================
# 8. for 루프와 리스트
# ============================================================
# for 루프는 리스트의 각 항목을 하나씩 꺼내 반복합니다.

supplies = ['pens', 'staplers', 'binders']
for item in supplies:
	print(item)
# pens
# staplers
# binders

# range(len(리스트))로 인덱스와 값을 동시에 사용할 수 있습니다.
for i in range(len(supplies)):
	print('인덱스', i, '→', supplies[i])


# ============================================================
# 9. in / not in 연산자
# ============================================================
# 리스트 안에 특정 값이 있는지 확인합니다.

spam = ['cat', 'bat', 'rat']
print('cat' in spam)      # True
print('dog' in spam)      # False
print('dog' not in spam)  # True


# ============================================================
# 10. 다중 할당 트릭 (Multiple Assignment / Tuple Unpacking)
# ============================================================
# 리스트의 값을 여러 변수에 한 번에 대입할 수 있습니다.
# 변수 개수와 리스트 항목 수가 반드시 같아야 합니다.

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat  # 한 줄로 세 변수에 대입합니다.
print(size)       # 'fat'
print(color)      # 'gray'
print(disposition)  # 'loud'


# ============================================================
# 11. enumerate() — 인덱스와 값 동시에 얻기
# ============================================================
# enumerate()는 루프마다 (인덱스, 값) 쌍을 반환합니다.

supplies = ['pens', 'staplers', 'binders']
for index, item in enumerate(supplies):
	print('인덱스', index, '→', item)
# 인덱스 0 → pens
# 인덱스 1 → staplers
# 인덱스 2 → binders


# ============================================================
# 12. random 모듈 — 리스트와 함께 사용하기
# ============================================================
import random

pets = ['Dog', 'Cat', 'Moose']

# random.choice(): 리스트에서 무작위로 하나 선택합니다.
print(random.choice(pets))   # 실행할 때마다 다른 결과가 나옵니다.

# random.shuffle(): 리스트 항목 순서를 무작위로 섞습니다. (제자리 변경)
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)  # 실행할 때마다 순서가 다르게 나옵니다.


# ============================================================
# 13. 복합 할당 연산자 (Augmented Assignment Operators)
# ============================================================
# spam = spam + 1  →  spam += 1  처럼 줄여쓸 수 있습니다.

spam = 10
spam += 3   # spam = spam + 3  →  13
spam -= 2   # spam = spam - 2  →  11
spam *= 2   # spam = spam * 2  →  22
spam //= 4  # spam = spam // 4 →  5
print(spam)  # 5

# 리스트와 문자열에도 사용 가능합니다.
my_list = ['a']
my_list *= 3
print(my_list)  # ['a', 'a', 'a']


# ============================================================
# 14. 리스트 메서드 (List Methods)
# ============================================================
# 메서드는 특정 값에 점(.)을 붙여 호출하는 함수입니다.

spam = ['hello', 'hi', 'howdy', 'heyas']

# index(): 값의 인덱스를 반환합니다. 없으면 ValueError 발생합니다.
print(spam.index('hi'))     # 1
print(spam.index('heyas'))  # 3

# 중복 값이 있으면 첫 번째 인덱스를 반환합니다.
dup = ['cat', 'dog', 'cat']
print(dup.index('cat'))  # 0 (두 번째 'cat'은 무시)


# append(): 리스트 끝에 항목을 추가합니다.
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)  # ['cat', 'dog', 'bat', 'moose']

# insert(): 지정한 인덱스 위치에 항목을 삽입합니다.
spam.insert(1, 'chicken')
print(spam)  # ['cat', 'chicken', 'dog', 'bat', 'moose']

# append()와 insert()는 반환값이 None이므로 spam = spam.append(...)처럼 쓰면 안 됩니다.


# remove(): 지정한 값을 첫 번째 것만 제거합니다. 없으면 ValueError 발생합니다.
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)  # ['cat', 'rat', 'elephant']

# 중복 값이 있을 때 첫 번째만 제거합니다.
spam2 = ['cat', 'bat', 'cat', 'hat']
spam2.remove('cat')
print(spam2)  # ['bat', 'cat', 'hat']


# sort(): 리스트를 오름차순으로 정렬합니다. (제자리 변경)
nums = [2, 5, 3.14, 1, -7]
nums.sort()
print(nums)  # [-7, 1, 2, 3.14, 5]

words = ['Ants', 'Cats', 'Dogs', 'Badgers']
words.sort()
print(words)  # ['Ants', 'Badgers', 'Cats', 'Dogs']

# 내림차순 정렬은 reverse=True를 사용합니다.
words.sort(reverse=True)
print(words)  # ['Dogs', 'Cats', 'Badgers', 'Ants']

# 대소문자 구분 없이 정렬하려면 key=str.lower를 사용합니다.
mixed_case = ['a', 'Z', 'B', 'z']
mixed_case.sort(key=str.lower)
print(mixed_case)  # 대소문자 무관하게 알파벳 순으로 정렬됩니다.

# sort()도 반환값이 None이므로 nums = nums.sort()처럼 쓰면 안 됩니다.


# reverse(): 리스트 순서를 뒤집습니다. (제자리 변경)
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)  # ['moose', 'dog', 'cat']


# ============================================================
# 15. 시퀀스 데이터 타입 (Sequence Types)
# ============================================================
# 리스트, 문자열, range 객체는 모두 시퀀스 타입입니다.
# 인덱싱, 슬라이싱, for 루프, len(), in/not in 모두 사용 가능합니다.

name = 'Zophie'
print(name[0])     # 'Z'
print(name[-2])    # 'i'
print(name[0:4])   # 'Zoph'
print('Zo' in name)  # True


# ============================================================
# 16. 가변(Mutable) vs 불변(Immutable)
# ============================================================
# 리스트 → 가변(mutable): 항목을 추가/제거/변경할 수 있습니다.
# 문자열, 튜플 → 불변(immutable): 한 번 만들면 내부를 바꿀 수 없습니다.

# 문자열은 인덱스로 값을 변경할 수 없습니다.
name = 'Zophie a cat'
# name[7] = 'the'  # → TypeError 발생합니다!

# 문자열을 "수정"하려면 슬라이싱으로 새 문자열을 만들어야 합니다.
new_name = name[0:7] + 'the' + name[8:12]
print(new_name)  # 'Zophie the cat'
print(name)      # 'Zophie a cat' (원본은 변경 안 됩니다)


# ============================================================
# 17. 튜플 (Tuple)
# ============================================================
# 튜플은 리스트와 비슷하지만 불변(immutable)입니다.
# 소괄호 ()로 작성합니다.

eggs = ('hello', 42, 0.5)
print(eggs[0])   # 'hello'
print(eggs[1:3]) # (42, 0.5)
print(len(eggs)) # 3

# 튜플은 값을 변경할 수 없습니다.
# eggs[1] = 99  # → TypeError 발생합니다!

# 항목이 하나인 튜플은 뒤에 쉼표를 붙여야 합니다.
print(type(('hello',)))  # <class 'tuple'>
print(type(('hello')))   # <class 'str'> (쉼표 없으면 그냥 문자열)

# list()와 tuple()로 서로 변환 가능합니다.
print(list(('cat', 'dog', 5)))  # ['cat', 'dog', 5]
print(tuple(['cat', 'dog', 5])) # ('cat', 'dog', 5)
print(list('hello'))            # ['h', 'e', 'l', 'l', 'o']


# ============================================================
# 18. 참조 (References)
# ============================================================
# 변수는 값 자체를 저장하는 게 아니라 값이 있는 메모리 주소(참조)를 저장합니다.

# 정수/문자열 같은 불변 타입은 복사할 때 새로운 값으로 독립됩니다.
spam = 42
eggs = spam
spam = 99
print(spam)  # 99
print(eggs)  # 42 (spam이 바뀌어도 eggs는 영향 없음)

# 리스트는 복사해도 같은 리스트를 가리킵니다! (참조 복사)
spam = [0, 1, 2, 3]
eggs = spam          # 같은 리스트를 가리킵니다.
eggs[1] = 'Hello!'
print(spam)  # [0, 'Hello!', 2, 3] ← spam도 바뀝니다!
print(eggs)  # [0, 'Hello!', 2, 3]

# 진짜 독립 복사본을 만들려면 copy 모듈을 사용합니다.
import copy

spam = ['A', 'B', 'C']
cheese = copy.copy(spam)   # 독립 복사본을 만듭니다.
cheese[1] = 42
print(spam)    # ['A', 'B', 'C'] (원본 그대로)
print(cheese)  # ['A', 42, 'C']

# 리스트 안에 리스트가 있으면 copy.deepcopy()를 사용합니다.
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0][0] = 99
print(nested)  # [[1, 2], [3, 4]] (원본 그대로)
print(deep)    # [[99, 2], [3, 4]]


# ============================================================
# 19. Short-Circuit (단락 평가)
# ============================================================
# and/or 연산자는 결과가 확정되면 나머지 평가를 건너뜁니다.
# 이를 활용해 빈 리스트로 인한 IndexError를 방지할 수 있습니다.

spam = []
# 잘못된 예: 빈 리스트면 IndexError 발생합니다.
# if spam[0] == 'cat': ...

# 올바른 예: len(spam) > 0이 False면 spam[0] 평가를 건너뜁니다.
if len(spam) > 0 and spam[0] == 'cat':
	print('cat이 첫 번째 항목입니다.')
else:
	print('리스트가 비어 있거나 첫 항목이 cat이 아닙니다.')
