#주어진 리스트 [5, 3, 9, 1, 8, 7]에서 짝수만 추출하고, 
#각 짝수의 제곱을 구한 후, 결과를 오름차순으로 정렬하여 출력하는 
#파이썬 함수를 작성하시오.

numberlist = [5, 3, 9, 1, 8, 7]
# process_list란 함수 선언
def process_list(numberlist):
    # 짝수만 추출 (for반복문 x변수 선언, numberlist에서, 만약 x변수 나누기 2가 0이면)
    even_numbers1 = [x for x in numberlist if x % 2 == 0]
    
    # 각 짝수의 제곱을 계산(for반복문 x변수에 제곱, 앞의 even_numbers1에서 뽑힌 수에서)
    squared_even_numbers2 = [x**2 for x in even_numbers1]
    
    # 결과를 오름차순으로 정렬(squared_even_numbers2에서 자체내부정렬)
    squared_even_numbers2.sort()
    # 함수값 반환 및 함수종료
    return squared_even_numbers2

# 결과는 process_list함수결과값(numberlist리스트안에서)
result = process_list(numberlist)
# result결과 출력
print(result)


# #[[덕덕고]]
# def extract_even_squares(numberlist):
#     even_squares = [x**2 for x in numberlist if x % 2 == 0]
#     even_squares.sort()
#     return even_squares

# # 사용 예시
# result = extract_even_squares(numberlist)
# print(result)  





  