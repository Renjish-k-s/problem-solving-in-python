l=input("enter the word").lower()

m=l[-1]

print(l)
print(l[:-1:].replace(m,'#')+m)

