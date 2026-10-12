class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}


        for s in strs:
            key = [0]*26
            for ch in s:
                key[ord(ch)-ord("a")] += 1

            key = tuple(key)
            if key not in group:
                group[key] = []
            group[key].append(s)


        return list(group.values())
                
