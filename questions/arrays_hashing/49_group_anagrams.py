# strs = ["eat","tea","tan","ate","nat","bat"]
# 1. create function to check anagram
# 2. create a dict of anagrams
# 3. go over the list and check if the str is in
#       the dict of anagrams
# 4. If yes, append to value (array) of that anagram
# 5. if no, create a new key and add this anagram 
# 6. return result as list of list

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}
        # ntlogt
        for s in strs:
            sorted_ana = "".join(sorted(s))  # O(tlogt)
            if sorted_ana in anagram_dict:
                anagram_dict[sorted_ana].append(s)
            else:
                anagram_dict[sorted_ana] = [s]
        
        return list(anagram_dict.values())
        
        
    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        
        def is_anagram(s, t):  # O(n)
            cha_dict = {}
            for cha in s:
                if cha in cha_dict:
                    cha_dict[cha] += 1
                else:
                    cha_dict[cha] = 1
            for cha in t:
                if cha in cha_dict:
                    cha_dict[cha] -= 1
                    if cha_dict[cha] == 0:
                        del cha_dict[cha]
                else:
                    return False
            return not cha_dict
        
        unique_anagrams = {}  # (anagram, strs)
        
        # O(n^3)
        for cur_str in strs:  # O(n)
            found = False
            for unique_anagram in unique_anagrams.keys():  # O(n)
                if is_anagram(cur_str, unique_anagram):  # O(n)
                    found = True
                    unique_anagrams[unique_anagram].append(cur_str)
                    break
            if not found:
                unique_anagrams[cur_str] = [cur_str]
        
        return list(unique_anagrams.values())
    
if __name__=="__main__":
    tc1 = ["eat","tea","tan","ate","nat","bat"]
    tc2 = [""]
    tc3 = ["a"]
    sol = Solution()
    print(sol.groupAnagrams(tc1))
    print(sol.groupAnagrams(tc2))
    print(sol.groupAnagrams(tc3))
