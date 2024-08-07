import random

class Dice:
    def __init__(self):
        self.numbers=[]
        
    def playDice(self):
        self.numbers.append(random,randint(1,6))
        
    def getNumbers(self):
        return self.numbers
    
    def getSum(self):
        return sum(self.numbers)
    
def sortNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse = True)
    return list
gamer1Dice=Dice()
gamer2Dice=Dice()
gamer3Dice=Dice()

for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()
print('Gamer1:',)