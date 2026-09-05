class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for word in strs:
            freq = [0]*26

            for ch in word:
                freq[ord(ch)-ord('a')] += 1

            key = tuple(freq)

            if key not in check:
                check[key] = []

            check[key].append(word)


        return list(check.values())