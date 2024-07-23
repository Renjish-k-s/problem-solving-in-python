stri="uudddduudduu"

stack=[]    

count=0
for i in stri:
    if stack and i=='d' and stack[-1]=='u':
        count+=1
    stack.append(i)

print(count)



#look up type problem
