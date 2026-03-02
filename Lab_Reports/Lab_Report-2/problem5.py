def dfs_path(grid, start, goal):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    path = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(x, y):
        visited[x][y] = True
        path.append((x, y))
        if (x, y) == goal:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    if dfs(nx, ny):
                        return True
        path.pop()
        return False

    if dfs(start[0], start[1]):
        print("Path found:")
        for p in path:
            print(p)
    else:
        print("No Path Found")

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

dfs_path(grid, (sx, sy), (gx, gy))