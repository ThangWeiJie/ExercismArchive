class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        specified_row = self.matrix_string.splitlines()[index - 1]
        return [int(n) for n in specified_row.split(' ')]

    def column(self, index):
        return [int(row.split()[index - 1]) for row in self.matrix_string.splitlines()]
