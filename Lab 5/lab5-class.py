#1.
# class stack:
#     def __init__(self, values) :
#         self.values = values

#     def push(self, value):
#         self.values.append(value)

#     def pop(self):
#         if len(self.values) == 0:
#             return None
#         else: 
#             self.values.pop(len(self.values) - 1)
#             return self.values   

#     def peek(self):
#         if len(self.values) == 0:
#             return None
#         else: return self.values[len(self.values) - 1]

#     def __str__(self):
#         return f"{self.values}"
    
# q1 = stack([1,2,3])
# print(q1)
# print(q1.pop())
# q1.push(4)
# print(q1)
# print(q1.peek())

#2.
# class Queue:
#     def __init__(self, values) :
#         self.values = values

#     def push(self, value):
#         self.values.append(value)

#     def pop(self):
#         if len(self.values) == 0:
#             return None
#         else: 
#             self.values.pop(0)
#             return self.values   

#     def peek(self):
#         if len(self.values) == 0:
#             return None
#         else: return self.values[0]

#     def __str__(self):
#         return f"{self.values}"
    
# q1 = Queue([1,2,3])
# print(q1)
# print(q1.pop())
# q1.push(4)
# print(q1)
# print(q1.peek())

#3.
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
        pass

    def apply_exp(self, exp):
        pass

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

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
print(m)
m.transpose()
print(m)