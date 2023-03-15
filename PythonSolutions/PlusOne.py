from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] < 9:
            digits[-1] += 1
        elif len(digits) > 1:
            digits = self.plusOne(digits[:len(digits) - 1])
            digits.append(0)
        else:
            digits[len(digits) - 1] = 0
            digits.insert(0, 1)
        return digits
