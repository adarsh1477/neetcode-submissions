class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
        ']':'[', '}':'{',')':'('
        }
        stack = []

        for ch in s:
            if not stack and ch in ")}]":
                return False
            elif ch in "({[":
                stack.append(ch)
            else:
                top = stack.pop()
                if pairs[ch] != top:
                    return False

        
        return True if len(stack) == 0 else False

        