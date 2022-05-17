class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            top = ''
            if stack != []:
                top = stack[-1]
            if c == top:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)