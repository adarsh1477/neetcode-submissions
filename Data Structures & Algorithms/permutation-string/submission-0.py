class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        first={}
        second={}
        for ch in s1:
            if ch not in first:
                first[ch]=1
            else:
                first[ch] += 1

        left=0
        for right,ch2 in enumerate(s2):
            if ch2 in second:
                second[ch2] += 1
            else:
                second[ch2] = 1
            while right-left>=len(s1):
                second[s2[left]] -= 1
                if second[s2[left]] == 0:
                    del second[s2[left]]
                left=left+1
            if first==second:
                return True
        return False

        