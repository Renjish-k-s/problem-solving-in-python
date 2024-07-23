string=input('ENTER THE SENTENCE').split()

def find_s(string):
    j=0
    for i in string:
        if(len(i)>2 and i[0]==i[-1]):
            j+=1
    return j

print(find_s(string))
    
