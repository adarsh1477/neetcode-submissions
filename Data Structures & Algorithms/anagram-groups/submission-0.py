class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check={}
        final=[]
        for ch in strs:
            key=sorted(ch)
            key=''.join(key)
            if key not in check:
                check[key]=[]
            check[key].append(ch)
               
        for key,value in check.items():
            final.append(value)
        return final
        