tokens = [100,200,300,400]
power = 200

start=0
end=len(tokens)-1
score=0
maxs=0
while start<=end:
    
    if tokens[start]<=power:
        power-=tokens[start]
        start+=1
        score=score+1
        
        if score>maxs:
            maxs=score
            
    elif score>0:
        power+=tokens[end]
        end-=1
        score-=1
    else:
        break
print(maxs)
        
    
