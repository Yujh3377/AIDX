class Book:
    def __init__(self,title,isbn):
        self.__title=title
        self.__isbn=isbn
    def __repr__(self):
        return "ISBN:"+self.__isbn+";Name:"+self.__title
    
class Mytime:
    def __init__(self,hour,minute,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return '%2d:%.2d:%.2d'%(self.hour,self.minute,self.second)
    
    
time=Mytime(10,25)
print(time)        
book=Book("python Tutorial","123544364")
book2=Book("The Machine Language","75686755")
print(book)
print(book2)