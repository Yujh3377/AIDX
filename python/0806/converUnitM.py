def convertUnit(lenMn):
    unitDic ={}
    unitDic['cm']=lenMn*0.1
    unitDic['m']=lenMn*0.001
    unitDic['inch']=lenMn*0.03937
    unitDic['ft']=lenMn*0.003281
    print(unitDic)
    return unitDic
def printLength(originalData,lengths):
    for len in lengths.keys():
        print(originalData,'mm -->',lengths[len],len)
            
