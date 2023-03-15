from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret_val = ""
        for i in range(len(strs[0])):
            possible_prefix = strs[0][:i + 1]
            for j in range(len(strs)):
                if self.isPrefix(strs[j], possible_prefix):
                    if j == len(strs) - 1:
                        ret_val = possible_prefix
                else:
                    return ret_val
        return ret_val


    def isPrefix(self, word: str, prefix: str) -> bool:
        return word[:len(prefix)] == prefix