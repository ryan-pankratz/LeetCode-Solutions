class Solution:
    def reverse(self, x: int) -> int:
        mult = 1
        var = str(x)[::-1]
        if x < 0:
            mult = -1
            var = var[:len(var) - 1]
        if mult * int(var) not in range((-2) ** 31, 2 ** 31):
            return 0
        else:
            return mult * int(var)
