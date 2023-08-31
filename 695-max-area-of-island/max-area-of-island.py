class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find_area(coord):
            area = 0
            stk = [coord]
            while stk:
                x, y = stk.pop()
                if visited[x][y] or grid[x][y] == 0:
                    continue

                # process
                area += 1
                visited[x][y] = True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x+dx < n and 0 <= y+dy < m:
                        stk.append((x+dx, y+dy))
            return area


        n = len(grid)
        m = len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        max_area = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] or grid[i][j] == 0:
                    continue
                max_area = max(max_area, find_area((i, j)))
        return max_area