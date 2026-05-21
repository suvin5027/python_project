# ================================================================
# [9일차 연습 미션] 회원 데이터 문자열 가공하기
# 파일명: test_20260519_mission.py
# 목표: split, join, replace 함수를 활용해 빈칸을 완성하시오.
# ================================================================

# [미션 1] split 미션: 콤마로 구분된 회원 목록 쪼개기
member_text = "수빈,우비,제나,부장님"

# 질문 1. member_text를 콤마(,) 기준으로 쪼개서 'member_list'라는 리스트에 담으삼
member_list = member_text.split(",")
print(member_list)  # 결과: ['수빈', '우비', '제나', '부장님']


# [미션 2] join 미션: 리스트를 슬래시(/)로 연결된 문자열로 합치기
# 질문 2. 위에서 만든 member_list의 알맹이들을 " / "로 연결해서 하나의 문자열로 출력해보삼
joined_text = " / ".join(member_text)
print(joined_text)  # 결과: "수빈 / 우비 / 제나 / 부장님"


# [미션 3] replace 미션: 잘못된 단어 수정하기
study_review = "오늘 파이썬 공부는 정말 지루하다!"

# 질문 3. .replace()를 사용해서 "지루하다"를 "보람차다"로 바꿔서 출력해보삼
fixed_review = study_review.replace("지루하다", "보람차다")
print(fixed_review)  # 결과: "오늘 파이썬 공부는 정말 보람차다!"