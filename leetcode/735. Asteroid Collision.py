def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack

# Test cases
asteroids1 = [10, 2, -5]
asteroids2 = [-2, -1, 1, 2]

print(asteroidCollision(asteroids1))  # Expected output: [10]
print(asteroidCollision(asteroids2))  # Expected output: [-2, -1, 1, 2]
