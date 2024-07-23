arr=[1,4,7,8,10]
arr.sort()
k=2
i=0
j=k-1
diff=arr[-1]-arr[0]

while j<len(arr):
    d=arr[j]-arr[i]
    if diff>d:
        diff=d
        a=arr[i]
        b=arr[j]
    i+=1
    j+=1
print(diff,a,b)
