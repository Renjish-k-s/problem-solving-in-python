order = "hucw"
s="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
res=""
for i in order:
    c=s.count(i)
    if c:
        res+=i*c
for i in s:
    if i not in res:
        c=s.count(i)
        res+=i*c
        
print(res)
