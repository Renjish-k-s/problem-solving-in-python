nums = [1,0,1,0,1]
goal = 2
l = 0
sumx = 0
c = 0

for r in range(len(nums)):
    sumx += nums[r]
    while l <= r and sumx >= goal:
        if sumx == goal:
            c += 1
        sumx -= nums[l]
        l += 1
        if l >= len(nums):  # Add this condition to prevent IndexError
            break

print(c)
