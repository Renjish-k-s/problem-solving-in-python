
fib1=0
fib2=1

n=10000000000000000n

for i in range(n):
    #print(fib1)
    temp=fib2
    fib2+=fib1
    fib1=temp
    
print(temp)
    
    
