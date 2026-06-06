class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for ch in strs:
            freq = [0]*26

            for c in ch:

                freq[ord(c) - ord('a')] += 1

            key = tuple(freq)

            if key not in check:
                check[key] = []
            check[key].append(ch)



        return list(check.values())