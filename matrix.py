import number

import pprint
pp = pprint.PrettyPrinter(indent=4)


def is_matrix(M):
    for row in M:
        for col in row:
            if not number.is_number(col):
                return False

    return True


def same_dimensions(A, B):

    if not is_matrix(A):
        return False
    if not is_matrix(B):
        return False

    if len(A) != len(B):
        return False
    if len(A[0]) != len(B[0]):
        return False

    return True


def multiply(k, M):

    if not is_matrix(M):
        print("not a matrix")
        return M
    kM = list()
    for row in M:
        new_row = list()
        for col in row:
            new_row.append(k * col)
        kM.append(new_row)

    return kM


def neg(M):

    return multiply(-1, M)


def Identity(N):

    M = list()
    for y in range(0, N-1):
        row = list()
        for x in range(0, N-1):
            if x == y:
                row.append(1)
            else:
                row.append(0)
        M.append(row)

    return M


def concat(A, B):
    if len(A) != len(B):
        return None

    Z = list()
    for i in range(0, len(A)):
        Z.append(A[i] + B[i])

    return Z


def append(A, B):
    if len(A[0]) != len(B[0]):
        return None

    Z = list()
    Z.append(A)
    Z.append(B)

    return Z


def Sylvester_construct(M, N):
    return


def Hadamard(N):
    M = [
        [1, 1],
        [1, -1]
    ]

    for n in range(0, N):

        Z = list()
        for i in range(0, len(M[0])):
            Z_row = list()
            for j in range(0, len(M)):

                if len(Z_row) < 1:
                    Z_row = multiply(M[i][j], M)
                else:
                    Z_row = concat(Z_row, multiply(M[i][j], M))

            if len(Z) < 1:
                Z = Z_row
            else:
                Z = append(Z, Z_row)
            pp.pprint(Z)

    return


def is_square(M):
    return
