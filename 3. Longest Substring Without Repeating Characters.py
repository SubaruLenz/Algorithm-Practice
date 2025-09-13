class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        keyWord = ""
        ans = 0

        for char in s:
            if char in keyWord:
                ans = max(ans, len(keyWord))
                keyWord = char
            else:
                keyWord += char
        return
                