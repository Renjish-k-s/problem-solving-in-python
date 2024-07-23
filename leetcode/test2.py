def root(num, tolerance=1e-7):
    x = 1
    while abs(x * x - num) > tolerance:
        x += 0.1
    return x

print(root(4))  # Expected output: a value close to 2.0
print(root(2))  # Expected output: a value close to 1.414
