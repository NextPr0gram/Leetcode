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
    words = strs
    sorted_words = []
    sorted_words_1 = []
    output = []
    for word in words:
        char_list = [char for char in word]
        sorted_char_list = sorted(char_list)
        sorted_words.append(sorted_char_list)
    
    first_word = sorted_words[0]
    for word in sorted_words:
        if word == first_word:
            output.append(words[sorted_words_1.index(word)])  
        sorted_words.remove(word)  
    return output
        

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))