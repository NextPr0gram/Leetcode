# Time limit exceeded
"""def containsDuplicate(nums) -> bool:
    nums_list = nums
    
    while True:
        count = 0
        current_num = nums_list[0]
        
        for num in nums:
            if num == current_num:
                count += 1
                
        if count > 1:
            return True
        elif len(nums_list) == 1:
            return False
        else :
            nums_list = nums_list[1:] # get rid of the first element"""

# Big O notation = O(n)
def containsDuplicate(nums) -> bool:
    # keys in a dictionary are unique, therefore no duplicates are allowed
    nums_dict = {}
    
    for num in nums:
        nums_dict[num] = 0
    print(nums_dict)
    
    keys = nums_dict.keys()
    # Since the keys are unique, if there were duplicates in the original list then the keys list will be shorter.
    if len(nums)> len(keys):
        return True
    else:
        return False
    
                
print(containsDuplicate([2,14,18,22,22]))