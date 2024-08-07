import numpy as np

arr1=[1,2,3,4]
arr2=[5,6,7,8]
twoDim =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDim)
print(twoDim[0][0])
print(twoDim[0][1])
print(twoDim[0][2])
A=np.array(arr1)
B=np.array(arr2)

result1 =A+B
result2 =arr1+arr2
result3 =A<3
print(result1)
print(result2)
print(result3)
