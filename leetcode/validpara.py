dicti={'{':'}','(':')','[':']'}

stri="{}{}{}"
stack=[]
c=0
for i in range(len(stri)):
    if stri[i] in dicti:
        stack.append(stri[i])
    elif len(stack)>0 and dicti[stack[-1]]==stri[i]:        
        stack.pop()
    else:
        print("not matching")
        c=1
        break
print(stack,c)
if len(stack)==0 and c==0:
    print("matching")
 

 
    



    
