def factorialNum(num):
    if num ==1:
        return 1
    else:
        return num * factorialNum(num -1)
    
num=int(input('숫자입력:'))

fact=1
for i in range(num,0,-1):
    
    fact *= i
    
print("{}!={}".format(num,fact))
print("{}!={}".format(num,factorialNum(num)))
