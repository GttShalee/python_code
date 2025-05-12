# 49. GroupAnagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # sort the each word and compare it with the sorted word
            # print(sorted_word)
            if sorted_word in anagrams:
                # if the sorted word is already in the dictionary(because it had be stored before), so append the word to the list
                anagrams[sorted_word].append(word)
            else:
                # if not, which means the sorted word is not in the dictionary, so create a new list and append the word to the list
                anagrams[sorted_word] = [word]
        # return the list of list
        return list(anagrams.values())
    
test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
