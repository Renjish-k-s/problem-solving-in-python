#n=input().rstrip()
#k=int(input().rstrip())
n=['a','a','b','b','c','c','c']
k=2
i=0
j=1

maxlen=0

while(i<=j and i<len(n) and j<=len(n)):
    print(n[i:j])
    chars=len(set(n[i:j]))
    if chars==k and maxlen<len(n[i:j]):
        maxlen=len(n[i:j])
    elif chars<k:
        j+=1
    elif chars>k:
        i+=1
    else:
        j+=1
print(maxlen)
        
