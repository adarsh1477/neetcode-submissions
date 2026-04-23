class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)

        start=0
        end=0

        def palindrome(s,left,right):
            while left >=0 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
            return right - left - 1


        for i in range(n):
            odd = palindrome(s,i,i)
            even = palindrome(s,i,i+1)

            length = max(odd,even)

            if length>end-start:

                start = i - (length-1) // 2
                end = i+length // 2

        return s[start:end+1]

