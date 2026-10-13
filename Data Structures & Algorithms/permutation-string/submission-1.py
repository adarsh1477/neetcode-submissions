from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_freq = Counter(s1)
        s2_freq = {}

        left = 0
        for right,ch in enumerate(s2):
            if ch not in s2_freq:
                s2_freq[ch] = 0
            s2_freq[ch] += 1

            while (right-left+1) > len(s1):
                s2_freq[s2[left]] -= 1
                
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]

                left +=1

            if s1_freq == s2_freq:
                return True


        return False