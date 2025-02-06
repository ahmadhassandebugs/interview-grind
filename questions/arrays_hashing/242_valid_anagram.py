# s = "anagram" t = "nagaram"
# hash s's counts and then remove from the dict
#   return False if count is zero or ele left in dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        