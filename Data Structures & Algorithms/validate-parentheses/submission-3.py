class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
        ']':'[', '}':'{',')':'('
        }


        check = []

        for ch in s:
            if ch in '({[':
                check.append(ch)
            else:
                if not check:
                    return False
                top = check.pop()
                if top != pairs[ch]:
                    return False

        if not check:
            return True
        return False