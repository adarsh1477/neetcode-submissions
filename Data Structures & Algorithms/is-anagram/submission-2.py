class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq,t_freq = {},{}
        if len(s)!=len(t): return False

        for i in range(len(s)):
            if s[i] not in s_freq:
                s_freq[s[i]] = 0
            s_freq[s[i]] += 1
            if t[i] not in t_freq:
                t_freq[t[i]] = 0
            t_freq[t[i]] += 1


        return s_freq == t_freq