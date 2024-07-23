address=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

for add in address:
    if add.count('@')==1:
        sp=add.split('@')
        local,domain=sp[0],sp[-1]
        if '+' in local and local.count('.')<=1:
            
            print(add)
   
