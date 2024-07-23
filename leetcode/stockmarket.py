#prices = [7, 1, 5, 3, 6, 4]#5
prices=[310,315,275,260,270,290,230,255,250]#30
size=len(prices)-1
buy=0
sell=1
maxi=0
while sell<size:
    if prices[buy]>=prices[sell]:
        buy=sell
    else:
        differ=prices[sell]-prices[buy]
        if differ>maxi:
            maxi=differ
    sell+=1
print(maxi)
    
    
