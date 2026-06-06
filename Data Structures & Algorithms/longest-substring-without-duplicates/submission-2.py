class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left=0
        best=0
        for right,ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

            while freq[ch]>1:
                freq[s[left]] -= 1
                left += 1

            best = max(best,right-left+1)

        return best
