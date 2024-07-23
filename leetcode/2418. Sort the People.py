def sortPeople(names, heights):
    length=len(names)
    for i in range(1,length):
        j=i-1
        while heights[i]>heights[j] and j>=0:
            heights[i],heights[j]=heights[j],heights[i]
            names[i],names[j]=names[j],names[i]
            i-=1
            j-=1
    print(names,heights)



names = ["Mary","John","Emma"]
heights = [180,165,170]
sortPeople(names, heights)
