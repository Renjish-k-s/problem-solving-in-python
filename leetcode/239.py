nums = [1,3,-1,-3,5,3,6,7]
k = 3
l=0
res=[]
for r in range(len(nums)):
    print(l,r)
    if r>=k-1:
        res.append(max(nums[l:r+1]))
        l+=1
print(res)
