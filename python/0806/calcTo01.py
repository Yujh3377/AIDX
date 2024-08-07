def calcTotalPrice(gps):
    dcRate =0;
    totalPrice=0
    
    if len(gps)==1:
        dcRate = 5;
    elif len(gps)==2:
        dcRate =20;
    elif len(gps)==3:
        dcRate =30;
        
        for item in gps:
            totalPrice += item * (1-dcRate/100)
            
        return [dcRate, totalPrice]
        