x=[1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4]
#x=list(map(int,input().rstrip().split(" ")))
j=1
i=0
leng=len(x)
while j<leng:
    if x[i]==x[j]:
        x.pop(j)
        leng-=1
    else:
        i+=1
        j+=1
print(x)
        
    
