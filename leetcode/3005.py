nums=[1,2,3,4,5]
c=0
dictx={i:count(i) for i in set(nums)}
maxx=max(dictx.values())
print(maxx)
for i in dictx.values():
    if i==maxx:
        c=c+maxx
print(c)
        
