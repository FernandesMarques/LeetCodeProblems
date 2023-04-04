def twoSum(nums, target):
    
    numbersofsum = []
    result = []
    
    for num in nums:
        i=1
        while i<len(nums):
            
            if (num+nums[i]) == target:
                numbersofsum.append(num) 
                numbersofsum.append(nums[i])
                i=len(nums)
            
            i=i+ 1
        if  len(numbersofsum) > 1:
            break
               
    for num in numbersofsum:
        i=0
        print(i)
        while i < len(nums):
            if nums[i] == num:
                result.append(i)
                i=len(nums)
            i=i+1
    print(result)   

    
twoSum([3,2,4],7)
