class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        check=[]

        for ch in s:
            if ch in '([{':
                check.append(ch)
            else:
                if not check:
                    return False
                top = check.pop()
                if top!=pairs[ch]:
                    return False

        if len(check)==0:
            return True
        else:
            return False

        