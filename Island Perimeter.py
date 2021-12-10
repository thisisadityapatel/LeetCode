class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        # Only for the first row:
        if grid[0][0] == 1:
            peri += 4
        for j in range(1, len(grid[0])):
            if grid[0][j] == 1:
                if grid[0][j-1] == 1:
                    peri += 4
                    peri -= 2
                else:
                    peri += 4
        # For rest of the rows
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    if grid[i][j] == 1:
                        if grid[i-1][j] == 1:
                            peri += 4
                            peri -= 2
                        else:
                            peri += 4
                else:
                    if grid[i][j] == 1:
                        if grid[i][j-1] == 1:
                            if grid[i-1][j] == 1:
                                peri += 4
                                peri -= 4
                            else:
                                peri += 4
                                peri -= 2
                        elif grid[i-1][j] == 1:
                            peri += 4
                            peri -= 2
                        else:
                            peri += 4
        return peri    