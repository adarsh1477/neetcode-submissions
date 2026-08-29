from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t): return ""
        window = Counter(t)
        res = [-1,-1]
        freq = {}
        required,have = len(window),0
        left = 0
        least = float('inf')

        for right,ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
            if ch in window and freq[ch] == window[ch]:
                have += 1


            while have == required:
                if right-left+1 < least:
                    res = [left,right]
                    least = right-left+1

                curr = s[left]
                freq[curr] -= 1

                if curr in window and freq[curr] < window[curr]:
                    have -= 1

                left += 1

        return s[res[0]:res[1]+1] if least!=float('inf') else ""
        







