def count_subarrays_with_sum(nums, goal):
    lrn = len(nums)
    c = 0
    window_sum = 0
    count_map = {0: 1}  # To handle subarrays starting from index 0

    for num in nums:
        window_sum += num
        if window_sum - goal in count_map:
            c += count_map[window_sum - goal]
        count_map[window_sum] = count_map.get(window_sum, 0) + 1

    return c

# Example usage:
nums = [1, 0, 1, 0, 1]
goal = 2
result = count_subarrays_with_sum(nums, goal)
print(result)
