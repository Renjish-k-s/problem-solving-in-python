class sol:
    def find(self,n):
        if n==1:return [[1]]
        output=self.find(n-1)
        print(output)
        
s=sol()
s.find(4)
