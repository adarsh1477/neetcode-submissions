from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        window = Counter(t)
        freq = {}
        least = float('inf')
        needed = len(window)
        have = 0
        index = [-1,-1]

        left = 0
        for right,ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

            if ch in window and freq[ch] == window[ch]:
                have += 1

            
            while have == needed:
                if right-left+1 < least:
                    least = right-left+1
                    index = [left,right]

                c = s[left]
                freq[c] -= 1

                if c in window and freq[c] < window[c]:
                    have -= 1

                left += 1


        return s[index[0]:index[1]+1] if least!=float('inf') else ""


