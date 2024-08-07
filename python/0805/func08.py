def addFunction(num):
	if num >0:
		print('num : ',num)
		addFunction(num -1)
		print('num = ',num)

addFunction(10)

