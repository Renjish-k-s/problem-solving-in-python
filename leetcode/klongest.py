string="araaajjjjjjjjjjfdnfvv"
d={}
l=0
k=2
maxlen=0
for r in range(len(string)):
    right_char=string[r]
    d[right_char]=d.get(right_char,0)+1
    while len(d)>k:
        left=string[l]
        d[left]=d.get(left)-1
        if d[left]==0:
            del d[left]
        l+=1
    maxlen=max(maxlen,r-l+1)
print(maxlen)
