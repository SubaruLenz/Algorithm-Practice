from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram_s = dict()
        for i in s:
            if i in anagram_s:
                anagram_s[i] += 1
            else:
                anagram_s[i] = 1
        anagram_t = anagram_s
        for i in t:
            if i not in anagram_t and anagram_t[i] == 0:
                return False
            anagram_t[i] -= 1
        return True