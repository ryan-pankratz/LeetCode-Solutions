class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        else:
            map_of_chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                            '9': 'wxyz'}
            L = []
            self._letterCombinations(digits, '', L, map_of_chars)
            return L

    def _letterCombinations(self, digits: str, current_str: str, combinations: List[str], map_1: Dict[str, str]):
        if len(digits) == 1:
            for c in map_1[digits[0]]:
                temp = current_str
                current_str += c
                combinations.append(current_str)
                current_str = temp
        else:
            for c in map_1[digits[0]]:
                temp = current_str
                current_str += c
                self._letterCombinations(digits[1:], current_str, combinations, map_1)
                current_str = temp