class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        count=0
        length = 32
        for ch in binary:
            count += 1

        binary = binary[::-1]
        r = length-count
        if r!=0:
            for i in range(r):
                binary += '0'

        return int(binary,2)
            
        