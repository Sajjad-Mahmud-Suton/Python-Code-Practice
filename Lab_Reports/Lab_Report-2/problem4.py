def dfs_traversal(grid, start, goal):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    directions = [(1,0,"Down"), (-1,0,"Up"), (0,1,"Right"), (0,-1,"Left")]

    def dfs(x, y):
        visited[x][y] = True
        print("Visited:", (x, y))
        if (x, y) == goal:
            return True
        for dx, dy, _ in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    if dfs(nx, ny):
                        return True
        return False

    if not dfs(start[0], start[1]):
        print("Goal not reachable")

# Main part
n = int(input("Enter grid size N: "))

grid = [
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 0]
]

print("\nGenerated Grid (0 = Free, 1 = Obstacle):")
for row in grid:
    print(row)

sx = int(input("\nEnter start x: "))
sy = int(input("Enter start y: "))
gx = int(input("Enter goal x: "))
gy = int(input("Enter goal y: "))

dfs_traversal(grid, (sx, sy), (gx, gy))