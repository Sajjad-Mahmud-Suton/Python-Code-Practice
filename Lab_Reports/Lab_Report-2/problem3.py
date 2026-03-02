from collections import deque

def bfs_path(grid, start, goal):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    parent = {}
    queue = deque()

    queue.append(start)
    visited[start[0]][start[1]] = True

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            break

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

    if goal not in parent and start != goal:
        print("No Path Found")
        return

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()

    print("Path from start to goal:")
    for p in path:
        print(p)

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

bfs_path(grid, (sx, sy), (gx, gy))