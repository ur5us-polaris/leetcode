
# Counting with a for loop. Could possibly implement a counter using a stack
class Solution:
    def countAndSay(self, n: int) -> str:
        # stop condition: if n == 1 return 1
        if n == 1:
            return '1'

        # if not, call with n-1
        say = self.countAndSay(n-1)
        # count the amount of contiguous sections
        res = ''
        counter = 1
        for i, c in enumerate(say):
            if i + 1 == len(say):
                res += str(counter) + c
                break
            if say[i + 1] == c:
                counter += 1
            else:
                res += str(counter) + c
                counter = 1
        return res


s = Solution()
print(s.countAndSay(4))



