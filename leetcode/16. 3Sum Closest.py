def threeSumClosest(nums,target):

    cdis=float('inf')
    
    
    nums.sort()
    j=2
    i=0
    dis=0
    leng=len(nums)
    print(nums)
    while j<leng:
        tempsum=sum(nums[i:j+1])
        print(nums[i:j+1],tempsum)

        form=tempsum
        to=target
        if form>to:
            form,to=to,form

        #print(form,to)
        for _ in range(form,to):
            dis+=1
       # print(dis)
        if dis<cdis:
            cdis=dis
            res=tempsum
        
        j+=1
        i+=1
        tempsum=0
        dis=0
        
    #print(res)
            
    
    






nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
threeSumClosest(nums,target)
