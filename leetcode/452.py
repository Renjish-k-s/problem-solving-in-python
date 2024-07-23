points =  [[1,2],[3,4],[5,6],[7,8]]
points.sort()
print(points)
j=1
res=[]
c=0
while j<len(points):
    if points[j-1][1]>points[j][0]:
        c+=1
        points[j]=[min(points[j-1][0],points[j][0]),max(points[j-1][1],points[j][1])]
    else:
        res.append(points[j-1])
    j+=1
res.append(points[j-1])
print(res,c)
