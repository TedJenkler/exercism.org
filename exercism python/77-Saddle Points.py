def saddle_points(matrix):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    if not matrix:
        return []

    saddle_points = []

    for row_idx, row in enumerate(matrix):
        row_max = max(row)
        
        col_indices = [col_idx for col_idx, value in enumerate(row) if value == row_max]

        for col_idx in col_indices:
            col_values = [matrix[r][col_idx] for r in range(len(matrix))]

            if row_max <= min(col_values):
                saddle_points.append({"row": row_idx + 1, "column": col_idx + 1})

    return saddle_points