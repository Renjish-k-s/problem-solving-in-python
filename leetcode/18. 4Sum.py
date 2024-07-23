class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        leng = len(nums)
        
        for i in range(leng - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number
            for j in range(i + 1, leng - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for the second number
                k = j + 1
                l = leng - 1
                while k < l:
                    csum = nums[i] + nums[j] + nums[k] + nums[l]
                    if csum > target:
                        l -= 1
                    elif csum < target:
                        k += 1
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1  # Skip duplicates for the third number
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1  # Skip duplicates for the fourth number
                        k += 1
                        l -= 1
                        
        return result

# Example usage:
nums = [2, 2, 2, 2, 2]
target = 8
solution = Solution()
print(solution.fourSum(nums, target))  # Output: [[2, 2, 2, 2]]
