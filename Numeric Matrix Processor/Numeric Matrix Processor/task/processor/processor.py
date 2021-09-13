class Matrix:
    def __init__(self, matrix=()):
        if matrix is not tuple:
            matrix = tuple(matrix)
        self.matrix = matrix

    def transpose(self, option=1):
        result_matrix = []

        if option == 1:
            for _ in self.matrix[0]:
                result_matrix.append([])
            for row in self.matrix:
                for i in range(len(result_matrix)):
                    result_matrix[i].append(row[i])
        elif option == 2:
            for _ in self.matrix[0]:
                result_matrix.append([])
            for row in self.matrix:
                for i in range(len(result_matrix)):
                    result_matrix[-i - 1].insert(0, row[i])
        elif option == 3:
            for row in self.matrix:
                result_matrix.append([])
                for val in row:
                    result_matrix[-1].insert(0, val)
        elif option == 4:
            for row in self.matrix:
                result_matrix.insert(0, row)

        return Matrix(result_matrix)

    def add(self, matrix):
        result_matrix = []
        for row_index, a_row in enumerate(self.matrix):
            result_matrix.append([])
            for column_index, a_val in enumerate(a_row):
                result = a_val + matrix.matrix[row_index][column_index]
                result_matrix[-1].append(result)
        return Matrix(result_matrix)

    def multiply_by_constant(self, constant):
        result_matrix = []
        for row in self.matrix:
            result_matrix.append([])
            for val in row:
                result = val * constant
                result_matrix[-1].append(result)
        return Matrix(result_matrix)

    def multiply_by_matrix(self, matrix):
        result_matrix = []
        for a_row in self.matrix:
            result_matrix.append([])
            for b_row in matrix.transpose().matrix:
                result = 0.0
                for i in range(len(a_row)):
                    result += a_row[i] * b_row[i]
                result_matrix[-1].append(result)
        return Matrix(result_matrix)

    def cofactor(self, i, j):
        m = [row[:j] + row[j + 1:] for row in self.matrix[:i] + self.matrix[i + 1:]]
        return pow(-1, i + j) * Matrix(m).determinant()

    def determinant(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        res = 0
        for i in range(len(self.matrix[0])):
            res += self.matrix[0][i] * self.cofactor(0, i)
        return res

    def print(self):
        for row in self.matrix:
            for val in row:
                print(int(val) if int(val) == val else val, end=" ")
            print()

    def inverse(self):
        m = [[self.cofactor(i, j) for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(m).transpose().multiply_by_constant(1 / self.determinant())


def get_one_matrix():
    a = []

    a_size = [int(e) for e in input("Enter size of matrix: ").split(" ")]
    print("Enter matrix:")
    for _ in range(a_size[0]):
        a.append([float(e) for e in input().split(" ")])

    return [Matrix(a), a_size]


def get_two_matrices():
    a = []
    b = []

    a_size = [int(e) for e in input("Enter size of first matrix: ").split(" ")]
    print("Enter first matrix:")
    for _ in range(a_size[0]):
        a.append([float(e) for e in input().split(" ")])

    b_size = [int(e) for e in input("Enter size of second matrix: ").split(" ")]
    print("Enter second matrix:")
    for _ in range(b_size[0]):
        b.append([float(e) for e in input().split(" ")])

    return [Matrix(a), Matrix(b), a_size, b_size]


def add_matrices():
    a, b, a_size, b_size = get_two_matrices()

    if a_size != b_size:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        a.add(b).print()


def multiply_matrix_by_a_constant():
    a, a_size = get_one_matrix()

    constant = float(input("Enter constant: "))
    print("The result is:")
    a.multiply_by_constant(constant).print()


def multiply_matrices():
    a, b, a_size, b_size = get_two_matrices()

    if a_size[1] != b_size[0]:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        a.multiply_by_matrix(b).print()


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    option = int(input("Your choice: "))

    a, a_size = get_one_matrix()

    print("The result is:")
    a.transpose(option).print()


def calculate_a_determinant():
    a, a_size = get_one_matrix()

    if a_size[0] != a_size[1]:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        det = a.determinant()
        print(int(det) if int(det) == det else det)


def inverse_matrix():
    a, a_size = get_one_matrix()

    if a.determinant == 0:
        print("This matrix doesn't have an inverse.")
    else:
        print("The result is:")
        a.inverse().print()


def start():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        option = input("Your choice: ")
        if option == "0":
            break
        elif option == "1":
            add_matrices()
        elif option == "2":
            multiply_matrix_by_a_constant()
        elif option == "3":
            multiply_matrices()
        elif option == "4":
            transpose_matrix()
        elif option == "5":
            calculate_a_determinant()
        elif option == "6":
            inverse_matrix()
        else:
            print("invalid input")
        print()


start()
