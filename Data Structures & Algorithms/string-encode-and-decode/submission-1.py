class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        final = []

        i=0
        j=1

        while i<len(s):
            while s[j]!='#':
                j += 1
            length = int(s[i:j])
            i=j+1
            j=i+length

            final.append(s[i:j])
            i=j


        return final