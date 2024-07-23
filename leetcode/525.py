nums=[1,1,0,0,1,1,0,1,1]
add=0
result=0
mapper={0:-1}
for key,value in enumerate(nums):

    if value==1:
        add+=value
    else:
        add-=1
    #print(add)

    if not add:
        if (key+1)>result:
            result=key+1
    elif add in mapper:
        temp=key-mapper[add]
        #print(key,mapper[add])
        if temp>result:
            result=temp
    else:
        mapper[add]=key
print(result)
#print(mapper)
