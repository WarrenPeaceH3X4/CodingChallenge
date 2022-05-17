class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0
        
        size = len(s)
        dp = [0]*(size + 1)
        dp[size] = 1
         
        for i in range(size - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]
            if i + 1 < size and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i + 2]
        return dp[0]

solution = Solution()
print(solution.numDecodings('0'))