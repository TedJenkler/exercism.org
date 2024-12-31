def spiral_matrix(size):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    matrix = [[0] * size for _ in range(size)]

    current_number = 1
    row, col = 0, 0
    direction_index = 0

    while current_number <= size ** 2:
        matrix[row][col] = current_number
        current_number += 1

        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]

        if (0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]

    return matrix