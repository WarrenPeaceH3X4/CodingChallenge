class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            top = ''
            if stack:
                top, _ = stack[-1]
            if top == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        res = ''
        for c, count in stack:
            res += c*count
        return res

solution = Solution()
print(solution.removeDuplicates("deeedbbcccbdaa", 3))