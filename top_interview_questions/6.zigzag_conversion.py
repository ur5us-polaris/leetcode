class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # create grid
        grid = [''] * numRows
        curr_row = 0
        is_down = 1
        for i, c in enumerate(s):
            grid[curr_row] += c
            if is_down == 1:
                if curr_row >= numRows - 1:
                    is_down = -1
            else:
                if curr_row <= 0:
                    is_down = 1
            curr_row += is_down
        return ''.join(grid)


s = 'PAYPALISHIRING'
sol = Solution()
print(sol.convert(s, 3))

