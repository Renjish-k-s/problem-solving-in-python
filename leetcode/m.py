class shop:
    def __init__(self,name,qty):
        self.name=name
        self.qty=qty
    def pur(self):
        qty=int(input("enter the quantity"))
        self.qty+=qty
        print("\nPURCHSE SUCESS\n")
    def sale(self):
        qty=int(input("\nenter the quantity\n"))
        if(self.qty>qty):
              self.qty-=qty
              print("\sale sucess!!\n")
        else:
            print("no possible")
    def __str__(self):
        print("____________")
        print("NAME:",self.name)
        print("QUANTITY:",self.qty)
        return '_____________'

pen=shop('pen',12)
pencil=shop('pencil',34)
eraser=shop('eraser',12)

ch=True

while(ch):

    print(pen)
    print(pencil)
    print(eraser)

    print("\n1.purchase\n2.sale\n3.exit")
    ip=int(input())

    if(ip==1):
        print("choose item")
        print("\n1.pen\n2.pencil\n3.eraser")
        co=int(input())
        if(co==1):
            pen.pur()
        elif(co==2):
            pencil.pur()
        elif(co==3):
            eraser.pur()
        else:
            print("invalid input")
    elif(ip==2):
        print("choose item")
        print("\n1.pen\n2.pencil\n3.eraser")
        co=int(input())
        if(co==1):
            pen.sale()
        elif(co==2):
            pencil.sale()
        elif(co==3):
            eraser.sale()
        else:
            print("invalid input")
    elif(ip==3):
        print("exiting........")
        ch=False
    else:
        print("invalid input")
        
        
        

    
            
        
