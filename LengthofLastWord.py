class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==1 and s[0]!=' ':
            return 1
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                count += 1
            if count != 0 and s[i] == ' ':
                return count
        return count