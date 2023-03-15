class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        mult = 1
        if s[0] == '-':
            mult = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        acc = ''
        count = 0
        cond = True
        while count < len(s) and cond:
            if not s[count].isdigit():
                cond = False
            else:
                acc += s[count]
                count += 1

        if len(acc) == 0:
            return 0
        else:
            var = int(acc) * mult
            if var < (-2) ** 31:
                return (-2) ** 31
            elif var > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return var