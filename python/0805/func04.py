def add():
	print('덧셈결과 :',inputNumber1+inputNumber2)
def sub():
        print('뺄셈결과 :',inputNumber1-inputNumber2)
def mul():
        print('곱셈결과 :',inputNumber1*inputNumber2)
def div():
        print('나눗셈결과 :',inputNumber1/inputNumber2)
while True:

	selectOperator = int(input('연산자 선택. 1,덧셈, 2.뺼셈, 3.곱셈, 4.나눗셈, 5.종료'))
	inputNumber1 = float(input('첫번쨰숫자입력:'))
	inputNumber2 = float(input('두번쨰숫자입력:'))

	if(selectOperator==1):
		add()
	elif(selectOperator==2):
		sub()
	elif(selectOperator==3):
        	mul()
	elif(selectOperator==4):
        	div()
	elif(selectOperator==5):
        	break
	else:
		print('연산자 다시 선택')

