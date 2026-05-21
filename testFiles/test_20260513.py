# 선언 및 초기화
fruits = ["apple", "banana", "cherry"]

# 인덱싱(Indexing): 0부터 시작함
print(fruits[0])  # apple

# 슬라이싱(Slicing): 파이썬만의 대박 기능! 범위를 잘라냄
# [시작:끝] -> 끝 인덱스는 포함 안 함!
print(fruits[0:2])  # ['apple', 'banana']

# 추가 및 삭제
fruits.append("orange") # 맨 뒤에 추가 (자바의 add)
fruits.remove("apple")  # 특정 값 삭제