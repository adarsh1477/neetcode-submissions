class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check={}
        left=0
        best=0
        for i,ch in enumerate(s):
            if ch in check:
                check[ch] += 1
            else:
                check[ch]=1
            while check[ch]>1:
                check[s[left]] -= 1
                left=left+1
            best=max(best,i-left+1)

        return best
            

        