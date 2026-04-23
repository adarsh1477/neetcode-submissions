class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s,res = [],[]
        s.append(len(temperatures)-1)
        res.append(0)
        for i in range(len(temperatures)-2,-1,-1):
            while s and temperatures[i]>=temperatures[s[-1]]:
                s.pop()
            s.append(i)
            if len(s)==1:
                res.append(0)
            else:
                res.append(s[-2]-s[-1])

        
        return res[::-1]


        