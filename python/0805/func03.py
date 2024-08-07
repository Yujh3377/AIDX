def introKor():
	print('안녕')

def introEng():
        print('hello')

def introJap():
        print('고니찌와')
while True:

	selectNum=int(input('where are you from? 1.한국, 2.USA, 3.Japan,4.Exit'))

if(selectNum == 1):
	introKor()
elif(selectNum == 2):
	introEng()
elif(selectNum == 3):
	introJap()
elif(selectNum == 4):
        break()
else:
	introEng()
 
