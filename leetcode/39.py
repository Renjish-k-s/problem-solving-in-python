'''a,b=int(input('ENTER 1st NUMBERS')),int(input('ENTER 2nd NUMBRERS'))
sum_1=lambda a,b: a if a>b else b
print(sum_1(a,b))'''



#40)

'''
b=int(input('enter the number to check'))
result=lambda x:print('DIVISIBLE') if not x%5 else print('not divisible')
print(result(b))'''


'''string=input('enter the string collection').split()
l=list(filter(lambda x:len(x)>5,string))
print(l)'''

num=[12,13,1001,999,665]

l=list(map(lambda x:x+(x*.1) if x>1000 else x+(x*.05),num))
print(l)

'''num=1234

def sum_1(n):
   sum=0
   while(n!=0):
       sum=sum+n%10
       n=n//10
   return sum

print(sum_1(num))'''
