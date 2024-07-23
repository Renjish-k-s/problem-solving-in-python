can = [2,3,5,1,3]
extra = 3
maxi=max(can)
returnlist=[]

for i in can:
    returnlist.append(i+extra>=maxi )
print(returnlist)
    
