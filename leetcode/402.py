num = "1432219"
k = 3
stack=[]
for i in num:
    while k>0 and stack and stack[-1]>i:
        stack.pop()
        k-=1
    stack.append(i)
while k>0:
    stack.pop()
    k-=1

res="".join(stack)

print(res)
