def path_finder(maze):
    maze = [list(row) for row in maze.split("\n")]
    n = len(maze)
    visited = [[False] * n for _ in range(n)]

    def dfs(row, col):
        if row == n - 1 and col == n - 1:  # Reached the exit
            return True

        if row < 0 or col < 0 or row >= n or col >= n:  # Out of bounds
            return False

        if visited[row][col] or maze[row][col] == 'W':  # Already visited or wall
            return False

        visited[row][col] = True

        # Explore adjacent cells in the four cardinal directions
        if dfs(row - 1, col):  # North
            return True
        if dfs(row, col + 1):  # East
            return True
        if dfs(row + 1, col):  # South
            return True
        if dfs(row, col - 1):  # West
            return True

        return False

    # Start DFS from the initial position (0, 0)
    return dfs(0, 0)
