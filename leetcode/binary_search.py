def binary_search(arr,ele):
    start,end=0,len(arr)-1

    while start<=end:
        mid=(start+end)//2
        if arr[mid]==ele:
            return True
        elif arr[mid]<ele:
            start=mid+1
        else:
            end=mid-1
    return False
        
arr=[1,2,3,4,5,6,7]
tar=10
if(binary_search(arr,tar)):
    print("found")
else:
    print("not found")
    
