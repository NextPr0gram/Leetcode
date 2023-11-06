""" def twoSum(nums: list[int], target: int) -> list[int]:
    nums_list = sorted(nums, reverse=True)
    reversed_num_list = sorted(nums)
    
    high_num_index = 0
    
    for i in range(0, len(nums_list) - 1):
        if nums_list[i] < target:
            high_num_index = i
            break
    reversed_num_list.remove(nums_list[high_num_index])
    
    if len(reversed_num_list) == 1 :
        return [nums.index(reversed_num_list[0]), nums.index(nums_list[high_num_index])]
    else:
        for i in range(0, len(reversed_num_list) - 1):
            if reversed_num_list[i] + nums_list[high_num_index] == target:
                return [nums.index(reversed_num_list[i]), nums.index(nums_list[high_num_index])] """
            

def twoSum(nums: list[int], target: int) -> list[int]:
    i = 0
    j = 0
    sum = None
    while sum != target:
        
        if j == len(nums)-1:
            if i == len(nums)-2:
                break
            else:
                i += 1
            j = i + 1
        else:
            j += 1
        sum = nums[i] + nums[j]
    return [i, j]

print("passed") if twoSum([0,4,3,0], 0) == [0,3] else print("failed")
