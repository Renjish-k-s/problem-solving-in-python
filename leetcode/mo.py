from collections import Counter

no=int(input())
size=[int(x) for x in input().split()]
cost=0
m=int(input())
for _ in range(m):
    l=[int(x) for x in input().split()]
    for x in size:
        if x==l[0]:
            size.remove(x)
            cost+=l[1]
            break
print(cost)
            
            
    
