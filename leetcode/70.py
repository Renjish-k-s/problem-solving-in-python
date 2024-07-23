def fib(n):
    if n<=3:
        return n
    a,b=2,3
    for _ in range(3,n):
        c=a+b
        a=b
        b=c
    return c
print(fib(5))
        
