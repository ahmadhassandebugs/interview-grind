# "abcabcbb"
# this can be solved with a sliding window
#   characters must be unique b/w first and last element: l and r
#   the window size is variable
# to figure out if a window is unique, we can use a hash map O(1) insertion and search
# we keep adding elements to a window: increment r
# if incrementing r leads to a duplicate
#   increment l until the window is unique


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        l, r, longest_sbstr = 0, 0, 0
        counter = {}

        while r < len(s):

            counter[s[r]] = 1 + counter.get(s[r], 0)
            
            while counter[s[r]] > 1:  # that duplicate can be anywhere in the window
                counter[s[l]] = counter[s[l]] - 1
                l += 1

            r += 1

            if r - l > longest_sbstr:
                longest_sbstr = r - l


        return longest_sbstr


if __name__ == "__main__":
    tc1 = "abcabcbb"
    tc2 = "bbbb"
    tc3 = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(tc1))
    print(sol.lengthOfLongestSubstring(tc2))
    print(sol.lengthOfLongestSubstring(tc3))
