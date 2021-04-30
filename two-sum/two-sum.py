def twoSum(nums,target):
    answer=[]
    for i,num in enumerate(nums):
        if target-num in nums and target-num != num: # temporary fix
            answer+=[i]
    return answer
print(twoSum([3,2,4],6))
