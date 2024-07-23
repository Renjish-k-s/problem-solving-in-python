s="dvdf"
listx=[]
maxi=0
for i in s:
    if i not in listx:
        listx.append(i)
    
    else:
        listx=[]
    length=len(listx)
    if maxi<length:
        maxi=length
    
print(maxi)
        
        
