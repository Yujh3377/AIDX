class Car:
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        
    def setMake(self,make):
        self.make=make
    def getMake(self):
        return self.make
    def printInfo(self):
        return "메이커=" +self.make + ",모델="+self.model + self.color +str(self.price)
    
class ElectricCar(Car):
    def __init__(self,make,model,color,price,batterySize):
        super().__init__(make,model,color,price)
        self.batterySize=batterySize
    def setbatterySize(self,batterySize):
        self.batterySize=batterySize
    def getbatterySize(self,batterySize):
        return self.batterySize
    
def main():
    basicCar=Car("Hyondae","Avante","black",200000)
    print(basicCar.printInfo())
    myCar =ElectricCar("Tesla","Model S","white",10000,0)#
    myCar.setMake("Tesla")
    myCar.setbatterySize(60)
    print(myCar.getDesc())
    print(type(basicCar))
    print(type(myCar))
    print(type(1))
main()
   
    
