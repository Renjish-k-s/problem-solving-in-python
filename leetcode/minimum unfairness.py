arr=[1,4,7,8,10]
arr.sort()
k=2
i=0
j=k
diff=100000
res=[]
a=[]
while j<=len(arr):
    a=arr[i:j]
    mini=min(a)
    maxi=max(a)
    if diff>(maxi-mini):
        diff=mini-maxi
        res=a
    print(i,j)
    i+=1
    j+=1
    
    
print(res)
    
    
    
