# 주어진 넘파이 배열 arr = np.array([[1, 2, 3], [4, 5, 6]])에서 
# 배열의 평균, 표준편차, 그리고 중앙값을 계산하는 파이썬 코드를 작성하시오.

# numpy라이브러리 불러옴 줄여서 np
import numpy as np
# arr는 넘파이 행렬 리스트
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 평균 계산 (넘파이 mean함수는 엑셀의 average함수)
mean = np.mean(arr)
print(f"평균: {mean}")

# 표준편차 계산 (넘파이 std함수는 표준편차 함수)
std_dev = np.std(arr)
print(f"표준편차: {std_dev}")

# 중앙값 계산 (넘파이 median함수는 중간값 함수) 
median = np.median(arr)
print(f"중앙값: {median}")

# f-string이라고 불리는 문자열 포맷팅 방법을 의미
# 파이썬 3.6부터 도입된 f-string은 문자열 안에 
# 중괄호 {}를 사용하여 변수나 표현식을 직접 삽입할 수 있는 방식 출처:인터넷