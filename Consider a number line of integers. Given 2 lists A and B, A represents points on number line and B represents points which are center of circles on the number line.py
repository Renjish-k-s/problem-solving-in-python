a = [1, 5, 10]
b = [3, 7]
mp=[]
res=0
for i in a:
    m=float('inf')
    for j in b:
        #print(i,j,abs(i-j))
        x=abs(i-j)
        if m>x:
            m=x
    #print(m)
    if res<m:
        res=m
    
print(res)
