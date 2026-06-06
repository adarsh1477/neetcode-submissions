class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for ch in strs:
            key = sorted(ch)
            key = "".join(key)

            if key not in check:
                check[key] = []
            check[key].append(ch)


        return list(check.values())