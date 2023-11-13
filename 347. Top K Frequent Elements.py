def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums_frequency = {}
    
    output = []
    
    for num in nums:
        nums_frequency[num] = nums_frequency.get(num, 1) + 1
    
    for key, value in nums_frequency.items():
        

    for _ in range(k)
