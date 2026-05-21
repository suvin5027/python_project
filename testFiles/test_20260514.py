# 선언하기
days = ("월", "화", "수")

# 사용하기 (리스트랑 똑같음)
print(days[0]) # 결과: 월

# 1. 선언하기 (중괄호 사용)
user_info = {
	"name": "수빈",
	"job": "개발자"
}

# 2. 데이터 꺼내기 (Key 이름으로 찾기)
print(user_info["name"]) # 결과: 수빈

# 3. 새로운 데이터 추가하기 (자바의 put() 보다 훨씬 쉬움!)
user_info["level"] = "beginner"

print(user_info) # 결과: 수빈