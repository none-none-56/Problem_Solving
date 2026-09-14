class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie = 0
        child = 0

        result = 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                result += 1
                cookie += 1
                child += 1
            else:
                cookie += 1
        
        return result