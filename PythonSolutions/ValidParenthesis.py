class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}
        recent = []
        for char in s:
            if char in d:
                recent.append(char)
            elif char in d.values():
                if recent == [] or d[recent[-1]] != char:
                    return False
                else:
                    recent.pop()
        return recent == []