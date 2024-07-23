def insertion_sort(unsorted_list):

    length=len(unsorted_list)
    for i in range(1,length):
        j=i-1
        
        while unsorted_list[i]<unsorted_list[j] and j>=0:
            unsorted_list[i],unsorted_list[j]=unsorted_list[j],unsorted_list[i]
            i-=1
            j-=1
    return unsorted_list




unsorted_list=[5, 3, 4, 2, 1, 6, 7, 8, 9, -1]

print(insertion_sort(unsorted_list))
