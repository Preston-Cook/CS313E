#  File: TestCipher.py

#  Description:

#  Student's Name:

#  Student's UT EID:

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys
import itertools

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm


def rail_fence_encode(strng, key):
    ROW_LEN = len(strng)

    matrix = []
    for i in range(key):
        matrix.append([''] * ROW_LEN)

    j = 0
    for i in range(ROW_LEN):
        if j == 0:
            down = True
        elif j == key - 1:
            down = False

        matrix[j][i] = strng[i]

        if down:
            j += 1
        else:
            j -= 1

    return ''.join(itertools.chain(*matrix))


def rail_fence_decode(strng, key):
    ROW_LEN = len(strng)

    matrix = []
    for i in range(key):
        matrix.append([''] * ROW_LEN)

    j = 0
    for i in range(ROW_LEN):
        if j == 0:
            down = True
        elif j == key - 1:
            down = False

        matrix[j][i] = '*'

        if down:
            j += 1
        else:
            j -= 1

    for i in range(key - 1, -1, -1):
        for j in range(ROW_LEN - 1, -1, -1):
            if matrix[i][j] == '*':
                matrix[i][j] = strng[-1]
                strng = strng[:-1]

    for i in range(key):
        matrix.append([''] * ROW_LEN)

    decoded_text = ''

    j = 0
    for i in range(ROW_LEN):
        if j == 0:
            down = True
        elif j == key - 1:
            down = False

        decoded_text += matrix[j][i]

        if down:
            j += 1
        else:
            j -= 1

    return decoded_text


def filter_string(strng):
    s1 = ''
    for char in strng.lower():
        if char.isalpha():
            s1 += char
    
    return s1


def encode_character(p, s):
    p_val = ord(p) - 97
    s_val = ord(s) - 97
    total_mod = p_val + s_val % 26
    return chr(total_mod + 97)


def decode_character(p, s):
    return ""


def vigenere_encode(strng, phrase):
    return ""


def vigenere_decode(strng, phrase):
    return ""


def main():
    # read the plain text from stdin
    lines = sys.stdin.readlines()
    arr = []

    for i in range(0, len(lines), 2):
        pair = tuple(map(str.rstrip, lines[i: i + 2]))
        arr.append(pair)

    print('Rail Fence Cipher\n')

    plaintext, key = arr[0]
    encoded_text = rail_fence_encode(plaintext, int(key))

    print(f'Plain Text: {plaintext}')
    print(f'Key: {key}')
    print(f'Encoded Text: {encoded_text}')

    print()  # Prints single line

    encoded_text, key = arr[1]
    decoded_text = rail_fence_decode(encoded_text, int(key))

    print(f'Encoded Text: {encoded_text}')
    print(f'Key: {key}')
    print(f'Deocded Text: {decoded_text}')

    print()

    print('Vigenere Cipher\n')

    plaintext, pass_phrase = arr[2]

    # read the plain text from stdin

    # read the pass phrase from stdin

    # encrypt and print the encoded text using Vigenere cipher

    # read the encoded text from stdin

    # read the pass phrase from stdin

    # decrypt and print the plain text using Vigenere cipher

    # The line above main is for grading purposes only.
    # DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
