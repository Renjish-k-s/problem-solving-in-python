def romanToInt(s):
    numdict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res=0
    for i in range(len(s)):
        if i<len(s)-1 and numdict[s[i]]<numdict[s[i+1]]:
            res-=numdict[s[i]]
        else:
            res+=numdict[s[i]]
    return res
            






s = "III"
print(romanToInt(s))
