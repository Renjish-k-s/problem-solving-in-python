nums = [1,3,5,6]
tar = 2
head=0
tail=len(nums)-1
while head<=tail:
    mid=(head+tail)//2
    if nums[mid]==tar:
        print(mid)
        break
    elif nums[mid]<tar:
        head=mid+1
    elif nums[mid]>tar:
        tail = mid-1
    
print(mid+1)
        
