l=[[1]]
n=6
i=1
if n==1:
    print(l)
elif n>1:
    while i<n:
        last=l[-1]
        row=[]
        row.append(1)
        start=0
        left=1
        end=len(last)-1
        while start<end:
            print(start,end,left)
            row.append(last[start]+last[left])
            start+=1
            
            left+=1
            
            
        row.append(1)
        l.append(row)
        i+=1
print(l)
