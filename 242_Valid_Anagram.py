def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    
    for char in s:
        if char in s_dict.keys():
            s_dict[char] += 1
        else:
            s_dict[char] = 0
    
    for char in t:
        if char in t_dict.keys():
            t_dict[char] += 1
        else:
            t_dict[char] = 0
    
    if s_dict == t_dict:
        return True
    else:
        return False

print(isAnagram("cat", "car"))