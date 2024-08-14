# 두 개의 숫자를 입력받아 그 숫자의 최대공약수를 
# 계산하는 파이썬 함수를 작성하시오. 
# 함수 내에서 람다를 사용하여 두 숫자의 최소공배수를 
# 계산하는 함수를 정의하시오.

# math 불러옴
import math
# gcd_and_lcm 함수 선언
def gcd_and_lcm(a, b):
    # 최대공약수 계산 (인수 a,b를 사용하는 math의 최대 공약수 [gcd]함수 사용)
    gcd_value = math.gcd(a, b)
    
    # 람다를 사용하여 최소공배수 계산
    # 일회용 람다 함수로 def보다 간결한 [lcm] 함수 선언
    # {a,b}의 공통된 배수 중에서 가장 작은 배수 구하는 최소공배수 [lcm]함수 정의함 )
    lcm = lambda x, y: (x * y) // gcd_value
    
    # lcm 함수 호출
    lcm_value = lcm(a, b)
    
    return gcd_value, lcm_value

# a,b 값을 각각 입력하소
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))
# gcd_and_lcm함수로 생성된 gcd_value, lcm_value값을 정해진 메세지에 출력
gcd_value, lcm_value = gcd_and_lcm(a, b)
print(f" {a} 와 {b} 의 최대공약수 :{gcd_value}")
print(f" {a} 와 {b} 의 최소공배수 :{lcm_value}")

# f-string이라고 불리는 문자열 포맷팅 방법을 의미
# 파이썬 3.6부터 도입된 f-string은 문자열 안에 
# 중괄호 {}를 사용하여 변수나 표현식을 직접 삽입할 수 있는 방식 출처:인터넷