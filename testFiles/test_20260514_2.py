# [1. 튜플(Tuple): 읽기 전용 리스트]
# - 소괄호()를 사용하여 선언함
# - 한 번 생성하면 내부 값을 절대 수정/삭제할 수 없는 불변(Immutable)의 특성을 가짐
# - 요일, 설정값 등 데이터 무결성이 중요한 정보를 담을 때 사용함
days = ("월", "화", "수")


# [2. 딕셔너리(Dictionary): Key-Value 구조]
# - 중괄호{}를 사용하며, 자바의 HashMap이나 JSON 객체와 유사한 구조임
# - 인덱스 번호가 아닌 의미 있는 '키(Key)' 이름으로 데이터를 관리함
user_info = {
	"name": "수빈",
	"job": "개발자"
}


# [3. 데이터 접근 및 추가]
# - 대괄호[] 안에 키 이름을 넣어 값에 접근함
print(user_info["job"])

# - 존재하지 않는 키에 값을 대입하면 새로운 항목이 동적으로 추가됨
user_info["level"] = "beginner"


# [4. 딕셔너리 순회(반복문) 방식 3가지]

# 방법 1) 키(Key)를 사용하여 값에 접근하기
# - for i in dict: 라고 쓰면 i에는 키값만 하나씩 담김
# - dict[i] 형태를 통해 해당 키에 연결된 값(Value)을 추출함
for i in user_info:
	print(f"키: {i}, 값: {user_info[i]} \n =======")

# 방법 2) .items() 활용 (실무 강력 권장)
# - 키(k)와 값(v)을 동시에 변수에 담아 순회할 수 있어 가장 가독성이 좋음
for k, v in user_info.items():
	print(f"키2 : {k} / 값2 : {v} \n =======")

# 방법 3) .values() 활용
# - 키는 무시하고 알맹이(값) 정보만 필요할 때 사용함
for val in user_info.values():
	print(f"값 확인: {val}")