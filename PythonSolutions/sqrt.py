class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        not_same = True
        k = x
        while not_same:
            t = k - (k * k - x) / (2 * k)
            if int(t) == int(k):
                not_same = False
            k = t

        return int(k)