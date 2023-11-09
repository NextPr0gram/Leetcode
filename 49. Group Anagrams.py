"""def groupAnagrams(strs: list[str]) -> list[list[str]]:
    original_words = strs
    output = []
    while len(original_words) != 0:
        letters = [char for char in original_words[0]]
        anagrams = []
        for word in strs:
            for letter in letters:
                if letter not in word:
                    original_words.remove(word)
                    break
            anagrams.append(word)
        output.append(anagrams)
        
    return output
        

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
        
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())
        

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))