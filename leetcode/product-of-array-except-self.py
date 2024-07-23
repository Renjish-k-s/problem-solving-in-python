
nums=[0,0]
product=[]

for i in range(len(nums)):
    res=1
    for j in range(len(nums)):
            if i!=j:
                res*=nums[j]
    product.append(res)
print(product)
