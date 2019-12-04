import number

import pprint
pp = pprint.PrettyPrinter(indent=4)


def is_matrix(M):
    for row in M:
        for col in row:
            if not number.is_number(col):
                return False

    return True


def neg(M):

    if not is_matrix(M):
        print("not a matrix")
        return M

    neg_M = list()
    for row in M:
        new_row = list()
        for col in row:
            new_row.append(-1 * col)
        neg_M.append(new_row)

    return neg_M


def Identity(N):

    M = list()
    for y in range(0,N-1):
        row = list()
        for x in range(0,N-1):
            if x == y:
                row.append(1)
            else:
                row.append(0)
        M.append(row)

    return M


def Hadamard(N):
    return


def is_square(M):
    return
