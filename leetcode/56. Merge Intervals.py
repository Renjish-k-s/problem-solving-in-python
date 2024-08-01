intervals = [[1,3],[2,6],[8,10],[15,18]]

leng=len(intervals)

i=intervals[0][0]
m=intervals[0][1]
j=1
res=[]
while j<leng:
    if m>=intervals[j][0]:
        m=intervals[j][1]
        
    elif j<leng-1:
        res.append([i,intervals[j][1]])
    else:
        res.append(intervals[j])
        
    j+=1

print(res)
