h=[1,1,1,1]
k = 2
i=0
p=-1
m=0
res=0
while i<k:
    if(h[p]-m)<=0:
        break
    else:
        res+=(h[p]-m)
        p-=1
        m+=1
    i+=1
print(res)

    
