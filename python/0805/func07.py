def calculator(num1,num2):
	result1=num1+num2
	result2=num1-num2
	result3=num1*num2
	result4=num1/num2

	return(result1, result2, result3, result4)

inputNumber1=int(input('첫째정수를 입력하세요:'))
inputNumber2=int(input('둘떄정수를 입력하세요:'))

result=calculator(inputNumber1, inputNumber2)
print(type(result))
print('사칙연산 결과:', result)
print('덧셈:',result[0])
print('뺼셈:',result[1])
print('곱셈:',result[2])
print('나눗셈:',result[3])
