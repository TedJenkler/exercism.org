class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [list(map(int, row.split())) for row in matrix_string.split("\n")]
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0]) if self.rows > 0 else 0

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
            