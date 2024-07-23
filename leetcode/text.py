m=""
def swap_case(s):
    global m
    for i in s:
        if i.isupper():
            m+=i.lower()
        elif i.islower:
            m+=i.upper()
            
            
    return m

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
