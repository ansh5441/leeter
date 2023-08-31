class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[0 for i in range(m)] for j in range(n)]
        num_island = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] > 0:
                    continue
                if grid[i][j] == "0":
                    continue
                stack = [(i, j)]
                num_island += 1
                while len(stack) > 0:
                    
                    x, y = stack.pop()
                    if visited[x][y] > 0:
                        continue
                    visited[x][y] = num_island
                    for dx , dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= x + dx < n and 0 <= y + dy < m and grid[x+dx][y+dy] == "1":
                            stack.append((x+dx,y+dy))
        return num_island