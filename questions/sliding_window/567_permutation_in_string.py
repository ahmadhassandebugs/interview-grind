# "ab", "eidbaooo"
# s2 will have at least one s1's permutation if frequency count matches for the
#   sliding window of s1's length
#   1. build two counters and then compare s1's counter with s2
#   2. build a fixed sized (26) frequency array and compare the values b/w two
#   3. sort s1 and s2 substrings and compare
# 4. let's try to solve this using the sliding window and recursive approach
#   first, we need to find all permutations of s1
#   then, see if any of the permutations exist in s2
# get all permutations: "abcd" => fix a, itertate over rest of the elements and
#   append each and call it recursively. when length is the same as string, add 
#   to the list
#   so we need cur and remaining as function arguments

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  # O(m * n)

        counter_s1  = {}

        for c in s1:  # O(n)
            counter_s1[c] = 1 + counter_s1.get(c, 0)

        win_size = len(s1)

        for i in range(len(s2) - win_size + 1):  # O(m)

            counter_s2 = {}  # can be optimized 

            substr = s2[i:i+win_size]

            for c in substr:  # O(n)
                counter_s2[c] = 1 + counter_s2.get(c, 0)
            
            found = True
            for key, value in counter_s1.items():  # O(n)
                if key not in counter_s2 or counter_s2[key] < value:
                    found = False

            
            
            if found: return True
        
        return False
                    
        
        # permutations = []

        # def build_permutations(cur, rem):  # O(n * n!)
        #     if not len(rem):
        #         permutations.append(cur)
            
        #     for i in range(len(rem)):
        #         build_permutations(cur + rem[i], rem[:i] + rem[i+1:])
        
        # build_permutations("", s1)

        # for perm in permutations:  # O(n!)
        #     if perm in s2:  # O(m)
        #         return True
        
        # return False


if __name__ == "__main__":
    tc1 = "ab", "eidbaooo"
    tc2 = "ab", "eidboaoo"
    sol = Solution()
    print(sol.checkInclusion(*tc1))
    print(sol.checkInclusion(*tc2))
