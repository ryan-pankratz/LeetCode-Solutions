class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        elif n == 0:
            return 1.0
        else:
            flag = False
            if n < 0:
                n = abs(n)
                flag = True

            dic = {1: x}
            tot = x
            count = 1

            while count < n:
                keys = list(dic.keys())
                i = 1
                key = keys[len(keys) - i]
                while count + key > n:
                    i += 1
                    key = keys[len(keys) - i]

                tot *= dic[key]
                dic[key + count] = tot
                count += key

            if flag:
                return 1 / tot
            return tot
