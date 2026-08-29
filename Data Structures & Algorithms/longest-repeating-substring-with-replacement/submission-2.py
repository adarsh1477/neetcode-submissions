class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        best = 0
        freq = {}

        for right,ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
            max_freq = max(max_freq,freq[ch])

            while (right-left+1)-max_freq > k:
                freq[s[left]] -= 1
                left += 1

            best = max(best,right-left+1)


        return best
        