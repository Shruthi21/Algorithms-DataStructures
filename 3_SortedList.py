#Given the sorted list of distinct integers from 0-99
#for instance [0,1,2,50,50,52,75]. Your task is to
#produce a string that describes numbers missing from
#the list

def ProduceMissingNum(A):
    ReturnString=''
    MissingNum=[]
    StartNum = 0
    for i in range(0,100):
        if i not in A:
            MissingNum.append(i)
        else:
            MissingNum.append('*')
            
    
    for i in range(0,100):
        if MissingNum[i] == i:
            if StartNum ==0:
                StartNum = i

        else:
            if StartNum != 0:
                if StartNum == i-1:
                    ReturnString+= str(StartNum) + ','
                else:
                    ReturnString+= str(StartNum) + '-' + str(i-1)
                    ReturnString+= ','
                StartNum = 0
 
        
    ReturnString+= str(A[-1]+1) + '-'+ str(MissingNum[-1])
    return ReturnString
