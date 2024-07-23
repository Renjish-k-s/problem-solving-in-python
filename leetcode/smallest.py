nums=[2,1,5,2,3,2]
l=0
mini=float('inf')
s=7
add=0
for r in range(len(nums)):
    add+=nums[r]
    while add>=s:
        mini=min(mini,r-l+1)
        add-=nums[l]
        l+=1
print(mini)
    
