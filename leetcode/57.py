intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals.append(newInterval)
intervals.sort()
#print(intervals)
i=1
res=[j for i in intervals for j in i]
res.sort()

print(res)
m=res[0]
while i<len(res):
    m+=1
    if m==res[i]:
        

