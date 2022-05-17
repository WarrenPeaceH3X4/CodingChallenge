class Solution:
    def removeDuplicates(self, s: str) -> str:
        p = 0
        s = list(' ' + s)
        for i in range(len(s)):
            if s[p] != s[i]:
                p += 1
                s[p] = s[i]
            elif p != 0:
                p -= 1
        s = s[1:p + 1]
        return ''.join(s)

solution = Solution()
print(solution.removeDuplicates("abbaca"))