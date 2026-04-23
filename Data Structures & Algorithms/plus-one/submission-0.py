class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len((digits))
        final = [0]*(n+1)

        for i in range(len(digits)):
            final[i+1] = digits[i]

        check = False
        for i in range(len(digits)-1,-1,-1):
            if final[i+1] != 9:
                final[i+1] += 1
                check = True 
                break
            else:
                final[i+1] = 0

        if check:
            return (final[1:])
        else:
            final[0] = 1 
            return final


       