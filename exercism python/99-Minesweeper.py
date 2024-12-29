def annotate(board):
    if board == []:
        return []
    if not isinstance(board, list) or not all(isinstance(row, str) for row in board):
        raise ValueError("The board is invalid with current input.")
    
    row_lengths = {len(row) for row in board}
    if len(row_lengths) != 1:
        raise ValueError("The board is invalid with current input.")
    
    valid_chars = {' ', '*'}
    if any(char not in valid_chars for row in board for char in row):
        raise ValueError("The board is invalid with current input.")
    
    result = [list(row) for row in board]
    
    def count_adjacent_mines(board, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1),         (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == '*':
                count += 1
        return count
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == ' ':
                mine_count = count_adjacent_mines(board, r, c)
                if mine_count > 0:
                    result[r][c] = str(mine_count)
    
    result = [''.join(row) for row in result]
    
    return result