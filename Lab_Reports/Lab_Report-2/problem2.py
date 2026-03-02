from collections import deque

def bfs_with_moves(grid, start, goal):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    queue = deque()

    queue.append(start)
    visited[start[0]][start[1]] = True

    directions = [
        (1,0,"Moving Down"),
        (-1,0,"Moving Up"),
        (0,1,"Moving Right"),
        (0,-1,"Moving Left")
    ]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            print("Goal Reached!")
            return

        for dx, dy, move in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    print(move, "->", (nx, ny))
                    visited[nx][ny] = True
                    queue.append((nx, ny))

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

bfs_with_moves(grid, (sx, sy), (gx, gy))