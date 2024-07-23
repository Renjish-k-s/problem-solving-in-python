m=[1,1,1,1,1,1,1,2,2,2,2,2,3,4,5,6,7,8]

leng=len(m)
k=2
low=0
high=leng
while low<high:
    mid=(low+high)//2
    if m[mid]==k:
        print("hgiohijo")
        res=mid
        break       
    elif m[mid]>k:
        high=mid
    else:
        low=mid
print(res)
while m[res]==m[res-1]:
    res-=1
    
print(res)
