class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        best = 0
        left = 0
        for right,ch in enumerate(s):
            if ch not in check:
                check[ch] = 0
            check[ch] += 1

            while check[ch] > 1:
                check[s[left]] -= 1
                left += 1

            best = max(best,right-left+1)


        return best

