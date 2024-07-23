nums = [2,11,10,1,3]
k = 10
m=0
for _ in range(len(nums)):
    nums.sort()
    i=nums[0]
    j=nums[1]
    c=0
    if i<k:
        nums.append(i*2+j)
        c+=1
        nums.remove(i)
        nums.remove(j)
    else:
        break
    m+=1

print(m)
