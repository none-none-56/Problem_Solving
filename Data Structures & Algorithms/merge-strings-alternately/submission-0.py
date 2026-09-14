class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = min(word1, word2, key=len)
        longer = max(word1, word2, key=len)

        result = ""

        i = 0
        while i < len(shorter):
            result += word1[i] + word2[i]
            i += 1
        
        result += word1[i:] + word2[i:]

        return result