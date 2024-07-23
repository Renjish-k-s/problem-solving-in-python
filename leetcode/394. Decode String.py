def decodeString(s):

    tempstr=""
    result=""
    dig_stack=[]
    char_stack=[]
    num=0

    leng=len(s)

    for i in range(leng):
        if s[i].isdigit():
            if s[i+1].isdigit():
                num=(num*10)+int(s[i])
            else:
                num=(num*10)+int(s[i])
                dig_stack.append(num)
                num=0
            
            print(dig_stack)
        elif s[i]!=']':
            char_stack.append(s[i])
        else:
            while char_stack:
                if char_stack[-1]!='[':
                    tempstr+=char_stack.pop()
                else:
                    char_stack.pop()
                    break
            if char_stack and dig_stack:
                char_stack.append(tempstr*dig_stack.pop())
            elif dig_stack:
                tempstr=tempstr[::-1]
                result+=(tempstr*dig_stack.pop())
                
            else:
                result+=tempstr
        tempstr=""
    while char_stack:
        tempstr+=char_stack.pop()
    result+=tempstr[::-1]
    print(result,char_stack)




s =  "100[leetcode]"
decodeString(s)
