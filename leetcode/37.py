num=[1,2,3,4,5,6,237,7,8,9,10]

def even(num):
    for i in num:
        if i==237:
            break
        elif not i%2:
            print(i)
            
print(even(num))
