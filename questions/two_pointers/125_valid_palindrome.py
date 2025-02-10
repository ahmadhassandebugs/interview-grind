# s = "A man, a plan, a canal: Panama" True
# 1. remove non-alphanumeric, convert to lowercase
# 2. compare first and last words (two pointers)
#       if not equal, return False
#       if equal, move to the next comparison
# 3. stop when two pointers are equal or intersect

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [cha.lower() for cha in s if cha.isalnum()]
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]: return False
            l, r = l+1, r-1
        return True
    
if __name__=="__main__":
    pass
