# 제7장 - 사전과 데이터 구조화 | 연습 파일

# ============================================================
# [1] 딕셔너리 만들기 & 접근
# ============================================================

# 자기 자신을 설명하는 딕셔너리입니다.
me = {"name": "박수빈", "age": "32", "hobby": "게임"}

# 'name' 값을 출력합니다.
print(me["name"])

# 'city' 키-값 쌍을 추가합니다.
me["city"] = "서울"

# 딕셔너리를 출력합니다.
print(me)


# ============================================================
# [2] 값 변경 & 삭제
# ============================================================

score = {'math': 90, 'english': 85, 'science': 78}

# 'math' 점수를 95로 변경합니다.
score["math"] = 95

# 'history': 88 을 추가합니다.
score["history"] = 88

# 'science' 키-값을 삭제합니다.
del score["science"]

# 결과를 출력합니다.
print(score)


# ============================================================
# [3] keys(), values(), items()
# ============================================================

fruits = {'apple': 3, 'banana': 5, 'cherry': 2}

# 키만 출력합니다.
for k in fruits.keys():
	print(k)

# 값만 출력합니다.
for v in fruits.values():
	print(v)

# 키와 값을 함께 출력합니다.
for k, v in fruits.items():
	print(k, ":", v, "개")

# 키 목록을 리스트로 변환합니다.
print(list(fruits))


# ============================================================
# [4] in / not in 연산자
# ============================================================

person = {'name': '수빈', 'age': 25, 'job': '개발자'}

# 'name'이 person에 있는지 확인합니다.
print("name" in person)

# 'email'이 person에 없는지 확인합니다.
print("email" not in person)

# '개발자'가 person의 값 중에 있는지 확인합니다.
print("개발자" in person.values())

# 'job'이 person에 있으면 "직업 있음"을 출력합니다.
if "job" in person.keys():
	print("직업 있음")


# ============================================================
# [5] get() 메서드
# ============================================================

inventory = {'sword': 1, 'shield': 2, 'potion': 5}

# 'potion' 수량을 출력합니다. (없을 때 기본값 0)
print(inventory.get("potion", 0))

# 'arrow' 수량을 출력합니다. (없는 키 → 기본값 0 반환)
print(inventory.get("arrow", 0))

# 'gold' 수량을 출력합니다. (없을 때 기본값 '없음')
print(inventory.get("gold", "없음"))


# ============================================================
# [6] setdefault() 메서드
# ============================================================

settings = {'theme': 'dark', 'language': 'Korean'}

# 없는 키이므로 font_size: 14가 추가됩니다.
# 딕셔너리의 기존 값이 전부 str이라 타입 경고가 뜨지만 실행에는 문제없습니다.
settings.setdefault("font_size", 14)

# 이미 있는 키이므로 변경되지 않습니다.
settings.setdefault("theme", "light")

# 결과를 출력합니다.
print(settings)


# ============================================================
# [7] setdefault() 활용 — 글자 세기
# ============================================================

word = 'Banana'
letter_count = {}

# setdefault로 초기화 후 += 1로 글자 등장 횟수를 셉니다.
for v in word:
	letter_count.setdefault(v, 0)
	letter_count[v] += 1

print(letter_count)


# ============================================================
# [8] 중첩 딕셔너리
# ============================================================

students = {
	'수빈': {'math': 95, 'english': 88},
	'지훈': {'math': 72, 'english': 91},
	'민지': {'math': 85, 'english': 79},
}

# 수빈의 math 점수를 출력합니다.
print(students["수빈"]["math"])

# 모든 학생의 이름과 점수를 출력합니다.
for k, v in students.items():
	print(k + ":", v)

# 모든 학생의 english 평균 점수를 구합니다.
total = 0
for k, v in students.items():
	total += v.get("english", 0)
average = total / len(students)
print(average)
