class Matrix:
    def __init__(self, N, M):
        self.matrix = []
        self.rows = N
        self.cols = M
        for i in range(N):
            row = []
            for j in range(M):
                row.append(0)
            self.matrix.append(row)

    def set(self, N, M, val):
        self.matrix[N][M] = val

    def get(self, N, M):
        return self.matrix[N][M]
    
    def transpose(self):
        transposed_matrix = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.matrix[j][i])
            transposed_matrix.append(row)
        self.matrix = transposed_matrix
        self.rows, self.cols = self.cols, self.rows

    def multiplication(self, matrix2):
        if self.rows != matrix2.cols:
            print("Matricile nu pot fi inmultite.")
        result = Matrix(self.cols, matrix2.rows)

        for i in range(self.cols):
            for j in range(matrix2.rows):
                sum_val = 0
                for k in range(self.rows):
                    sum_val += self.matrix[k][i] * matrix2.matrix[j][k]
                result.set(j, i, sum_val)
        return result

    def apply_transformation(self, lambda_func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = lambda_func(self.matrix[i][j])

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self.matrix])

m = Matrix(3,3)
m.set(0, 0, 1)
m.set(0, 1, 2)
m.set(0, 2, 3)
m.set(1, 0, 4)
m.set(1, 1, 5)
m.set(1, 2, 6)
m.set(2, 0, 7)
m.set(2, 1, 8)
m.set(2, 2, 9)
print("Matricea initiala este: ")
print(m)
print("Matricea modificata cu functia x = x + 1 este: ")
m.apply_transformation(lambda x : x + 1)
print(m)
print("Matricea transpusa este: ")
m.transpose()
print(m)
m2 = Matrix(3,3)
m2.set(0, 0, 9)
m2.set(0, 1, 8)
m2.set(0, 2, 7)
m2.set(1, 0, 6)
m2.set(1, 1, 5)
m2.set(1, 2, 4)
m2.set(2, 0, 3)
m2.set(2, 1, 2)
m2.set(2, 2, 1)
print("A doua matrice este: ")
print(m2)
print("Rezultatul inmultirii celor doua matrici este: ")
print(m.multiplication(m2))
