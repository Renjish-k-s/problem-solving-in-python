strs = ["c","acc","ccc"]
common=strs[0]
i=1
while i<len(strs):
    s=len(common)
    print(common,strs[i][:s])
    
    if common not in strs[i][:s]:
        common=common[:-1]
    else:
        i+=1
    if not len(common):
        break
print(common)
