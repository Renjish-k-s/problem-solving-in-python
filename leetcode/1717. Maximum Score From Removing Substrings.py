def maximumGain(s,x,y):

    def remover(s,f,se,val):
        stack=[]
        
        ls=0
        for i in s:
            if stack and i==se and stack[-1]==f:
                stack.pop()
                ls+=val
            else:
                stack.append(i)
            
        return "".join(stack),ls
        

    a='a'
    b='b'
    if x>=y:
        s,score1=remover(s,a,b,x)
        s,score2=remover(s,b,a,y)
    else:
        s,score1=remover(s,b,a,y)
        s,score2=remover(s,a,b,x)

    print(score1+score2)
        

    










s = "cdbcbbaaabab"
x = 4
y = 5
maximumGain(s,x,y)
