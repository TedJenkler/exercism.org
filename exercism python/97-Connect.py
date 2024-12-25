class ConnectGame:
    def __init__(self, board):
        self.board = [list(row.strip().replace(" ", "")) for row in board.strip().split('\n')]

    def get_winner(self):
        n, m = len(self.board), len(self.board[0])

        def dfs(x, y, player, visited):
            if x < 0 or y < 0 or x >= n or y >= m or (x, y) in visited or self.board[x][y] != player:
                return False

            visited.add((x, y))

            if player == "O" and x == n - 1:
                return True
            if player == "X" and y == m - 1:
                return True

            neighbors = [
                (x - 1, y), (x + 1, y),
                (x, y - 1), (x, y + 1),
                (x - 1, y + 1), (x + 1, y - 1)
            ]
            return any(dfs(nx, ny, player, visited) for nx, ny in neighbors)

        for col in range(m):
            if self.board[0][col] == "O" and dfs(0, col, "O", set()):
                return "O"

        for row in range(n):
            if self.board[row][0] == "X" and dfs(row, 0, "X", set()):
                return "X"

        return ""