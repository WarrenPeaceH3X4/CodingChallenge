class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0
        
        size = len(s)
        
        def helper(i):
            if i >= size:
                return 1
            if s[i] == '0':
                return 0
            
            res = helper(i + 1)
            if i + 1 < size and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += helper(i + 2)
            return res
        
        return helper(0)

solution = Solution()
print(solution.numDecodings('26'))