nums=[1,8,6,2,5,4,8,3,7]
start=0
end=len(nums)-1
maxi=0
while start<end:
    if nums[start]<nums[end]:
        mini=nums[start]
    else:
        mini=nums[end]
        
    differ=end-start
    product=mini*differ
    if maxi<product:
        maxi=product
        
    if nums[start]<nums[end]:
        start+=1
    else:
        end-=1
print(maxi)
