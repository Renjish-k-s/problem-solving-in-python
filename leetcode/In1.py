word1 = "ab"
word2 = "pqrs"

w1=len(word1)
w2=len(word2)
wmax=max(w1,w2)

i=0
string=""

while i<wmax:

    if i<w1 and i<w2:

        string+=w1[i]
        string+=w2[i]
    elif i<w1:

        string+=w1[i]
    else:
        string+=w2[i]
    i+=1
