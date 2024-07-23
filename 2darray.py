mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
for i in range(len(mat[0])):
    for j in range(i):
        temp=mat[i][j]
        mat[i][j]=mat[j][i]
        mat[j][i]=temp
        
for r in mat:
    r.reverse()

for r in mat:
    print(r)
 m
