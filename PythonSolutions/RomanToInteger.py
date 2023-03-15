class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prev = d[s[0]]
        acc = 0
        for char in s:
            acc += d[char]
            if d[char] > prev:
                acc -= 2 * prev
            prev = d[char]
        return acc