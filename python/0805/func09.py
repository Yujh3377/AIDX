def factorialNum(num):
	if num==1:
		return 1
	else:
		return num * factorialNum(num-1)

inputData = int(input('0보다 큰숫자를 입력하세요.'))
result = factorialNum(inputData)
print('%d! = %d\n'% (inputData, result))
