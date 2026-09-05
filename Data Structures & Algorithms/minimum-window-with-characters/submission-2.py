from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        window = Counter(t)
        res = [-1,-1]
        freq = {}
        left = 0
        least = float('inf')
        have,required = 0,len(window)

        for right,ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0

            freq[ch] += 1

            if ch in window and window[ch] == freq[ch]:
                have += 1



            while have == required:
                if right-left+1 < least:
                    res = [left,right]
                    least = right-left+1

                c = s[left]
                freq[c] -= 1
                
                if c in window and freq[c] < window[c]:
                    have -= 1


                left += 1


        return s[res[0]:res[1]+1] if least!=float('inf') else ""

                
