apple = [5,5,5]
capacity = [2,4,2,7]

capacity.sort(reverse=True)
sumx=sum(apple)
c=0

while sumx>0:
    sumx-=capacity[c]
    c+=1
print(c)
