nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
i=0
j=0
common=0

while i<len(nums1) and j<len(nums2):
    if nums1[i]==nums2[j]:
        common=nums1[i]
        break
    elif(nums1[i]<nums2[j]):
        i+=1
    else:
        j+=1
print(common)if common else print("-1")
