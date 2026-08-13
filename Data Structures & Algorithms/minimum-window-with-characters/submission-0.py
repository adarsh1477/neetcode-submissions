from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) : return ""
        check = Counter(t)
        freq = {}
        curr, required = 0,len(check)
        res = [-1,-1]
        size = float('inf')

        left = 0
        for right in range(len(s)):
            c = s[right]
            if c not in freq: freq[c] = 0
            freq[c] += 1

            if c in check and freq[c] == check[c]:
                curr += 1

            while curr == required:
                if right-left+1 < size:
                    res = [left,right]
                    size = right - left + 1

                p = s[left]
                freq[p] -= 1

                if p in check and freq[p] < check[p]:
                    curr -= 1

                left += 1



        return s[res[0]: res[1]+1] if size!=float('inf') else ""



