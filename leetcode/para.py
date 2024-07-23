stri="{{{{}}}"
stack=[]
count=0
for i in stri:
    if i == '{':
        count+=1
    else:
        count-=1
    if count<0:
        print('invalid')
        break
print(count==0)
    
