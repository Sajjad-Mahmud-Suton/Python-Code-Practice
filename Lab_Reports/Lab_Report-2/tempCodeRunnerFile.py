import random
from collections import deque

def create_grid(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if random.randint(0, 4) == 0:   
                grid[i][j] = 1
    return grid

def print_grid(grid):
    print("\nGenerated Grid (0 = Free, 1 = Obstacle):")
    for row in grid:
        print(row)


def bfs_traversal(grid, start, goal):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    queue = deque()

    queue.append(start)
    visited[start[0]][start[1]] = True

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            print("Goal Reached!")
            return

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    print("No Path Found")


n = int(input("Enter grid size N: "))
grid = create_grid(n)
print_grid(grid)

sx = int(input("Enter start x: "))
sy = int(input("Enter start y: "))
gx = int(input("Enter goal x: "))
gy = int(input("Enter goal y: "))

bfs_traversal(grid, (sx, sy), (gx, gy))