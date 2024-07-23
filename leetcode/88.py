nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums1.extend(nums2)
nums1.sort()
nums1=[x for x in nums1 if x!=0]
print(nums1)
