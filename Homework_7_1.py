class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        tmp = ''
        for r in self.matrix:
            tmp += str(r).replace('[', '').replace(']', '').replace(',', '') + '\n'
        return tmp

        # print("{:4d}".format(x), end='')

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(other.matrix[i])):
                tmp.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(tmp)
        return '\n'.join(map(str, result)).replace('[', '').replace(']', '').replace(',', '')


matrix_1 = Matrix([[1, 2], [1, 2], [1, 2]])
matrix_3 = Matrix([[2, 5], [1, 1], [8, 8]])

print(matrix_1)
print(matrix_1 + matrix_3)
# print(['\n'.join(map(str, i)) for i in matrix_1 + matrix_3])
