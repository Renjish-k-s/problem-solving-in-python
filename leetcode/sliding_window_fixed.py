nums=[1,3,2,6,-1,4]
l=0
s=0
k=3
res=[]
maxi=0
for r in range(len(nums)):
    s+=nums[r]
    #print(s)
    if r>=k-1:
        #res.append(s)
        if s>maxi:
            maxi=s
        s-=nums[l]
        #print(nums[l])
        l+=1
print(maxi)
