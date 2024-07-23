nums = [2,0,2,1,1,0]
temp=[]
for i in range(3):
    c=nums.count(i)
    temp.extend([i]*c)
nums=temp
print(nums)
