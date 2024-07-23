fibno={1:0,2:1}

def fibino(fib1):
    if fib1==1:
        return 0
    elif fib1 ==2:
        return 1
    else:
        if(fib1 in fibno):
            return fibno[fib1]
        else:
            fibno[fib1]=fibino(fib1-1)+fibino(fib1-2)
            return fibno[fib1]


print(fibino(10000))
