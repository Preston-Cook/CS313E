#  File: WordSearch.py

#  Description: Solves a word search

#  Student Name: Preston Cook

#  Student UT EID: plc886

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: N/A

#  Date Created: 12/21/2022

#  Date Last Modified: 12/21/2022

import sys


def read_input():
    n = int(sys.stdin.readline())
    matrix, words = [], []

    next(sys.stdin)

    for _ in range(n):
        line = sys.stdin.readline()
        matrix.append(line.split())

    next(sys.stdin)

    n = int(sys.stdin.readline())

    for _ in range(n):
        line = sys.stdin.readline()
        words.append(line.rstrip())

    return (matrix, words)


def find_word(grid, word):
    GRID_LEN, WORD_LEN = map(len, (grid, word))

    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if grid[i][j] == word[0]:

                # Left
                if j + 1 >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i][j - z] != word[z]:
                            break
                    else:
                        return (i, j)

                # Right
                if GRID_LEN - j >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i][j + z] != word[z]:
                            break
                    else:
                        return (i, j)

                # Up
                if i + 1 >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i - z][j] != word[z]:
                            break
                    else:
                        return (i, j)

                # # Down
                if GRID_LEN - i >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i + z][j] != word[z]:
                            break
                    else:
                        return (i, j)

                # Top L diag
                if i + 1 >= WORD_LEN and (j + 1) - WORD_LEN >= 0:
                    for z in range(1, WORD_LEN):
                        if grid[i - z][j - z] != word[z]:
                            break
                    else:
                        return (i, j)

                # Top R diag
                if i + 1 >= WORD_LEN and GRID_LEN - j >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i - z][j + z] != word[z]:
                            break
                    else:
                        return (i, j)

                # Bottom L diag
                if GRID_LEN - i >= WORD_LEN and j + 1 >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i + z][j - z] != word[z]:
                            break
                    else:
                        return (i, j)

                # Bottom R diag
                if GRID_LEN - i >= WORD_LEN and GRID_LEN - j >= WORD_LEN:
                    for z in range(1, WORD_LEN):
                        if grid[i + z][j + z] != word[z]:
                            break
                    else:
                        return (i, j)


def main():
    # read the input file from stdin
    word_grid, word_list = read_input()

    # find each word and print its location
    for word in word_list:
        location = find_word(word_grid, word)
        print(word + ": " + str(location))


if __name__ == "__main__":
    main()
