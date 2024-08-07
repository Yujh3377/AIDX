class Student:
    def __init__(self, name=None, age=0):
        self.__name=name
        self.__age=age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age=age    
obj =Student("Hong",50)
print(obj.getAge())
obj.setAge(100)
print(obj.getAge())
