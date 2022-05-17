class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        q = collections.deque()
        q.append([0, 0, 1])
        grid[0][0] = 1
        n = len(grid)
        
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
        while q:
            r, c, length = q.popleft()
            
            if r == n - 1 and c == n -1:
                return length

            for dr, dc in directions:
                i = r + dr
                j = c + dc
                if 0 <= i < n and 0 <= j < n and not grid[i][j]:
                        q.append([i, j, length + 1])
                        grid[i][j] = 1 
        return -1