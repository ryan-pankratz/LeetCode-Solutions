class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = len(s) - 1
        length = 0
        while count >= 0 and s[count] == " ":
            count -= 1

        while count >= 0 and s[count].isalpha():
            length += 1
            count -= 1
        return length