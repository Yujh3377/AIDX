class Television2:
    objectCnt=0
    def __init__(self,channel,volume,on):
        self.channel =channel
        self.volume =volume
        self.on =on
        Television2.objectCnt +=1
        
        
    def show(self):
        print(self.channel,self.volume,self.on,self.objectCnt)
        
myTv =Television2(24,20,True)
myTv.show()
yourTv =Television2(21,25,False)
yourTv.show()
myTv.show()
