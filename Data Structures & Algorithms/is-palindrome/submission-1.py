class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(s)-1

        while left<=right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True