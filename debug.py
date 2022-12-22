from copy import deepcopy

def print_matrix(matrix):
    for row in matrix:
        print(row)

def zig_zag(matrix, key):
    copy = deepcopy(matrix)
    j = 0
    for i in range(len(copy[0])):
        if j == 0:
            down = True
        elif j == key - 1:
            down = False

        copy[j][i] = '*'

        if down:
            j += 1
        else:
            j -= 1

    return copy

matrix = [['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], ['', '', '', '', '', '', '']]
output = zig_zag(matrix, 3)
for row in output:
    print(row)