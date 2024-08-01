nums = [3,30,34,5,9]
reslis=[]

for i in nums:

    while i:

        
        reslis.append(i%10)
        i//=10
reslis.sort(reverse=True)
res=""
for i in reslis:

    res+=str(i)
print(res)
