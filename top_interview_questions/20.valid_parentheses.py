
closers = {
    ')': '(',
    ']': '[',
    '}': '{'
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == closers[c]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True



s = '([]){}'
sol = Solution()
print(sol.isValid(s))

