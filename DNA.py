#  File: DNA.py

#  Description: Finds longest nucleotide subsequence given two sequences of DNA

#  Student Name: Preston Cook

#  Student UT EID: plc886

#  Partner Name: N/A

#  Partner UT EID: plc886

#  Course Name: CS 313E

#  Unique Number: N/A

#  Date Created: 12/20/2022

#  Date Last Modified: 12/20/2022

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

import sys


def longest_subsequence(s1: str, s2: str) -> list[str]:
    """Generates a list of the longest subsequences in two strings without duplicates"""
    shortest, longest = sorted([s1, s2], key=len)

    shortest_len = len(shortest)

    common_subsequences = []

    for i in range(shortest_len):
        for j in range(i + 1, shortest_len + 1):
            substr = shortest[i:j]
            if substr in longest and len(substr) >= 2:
                if not common_subsequences or len(substr) > len(common_subsequences[0]):
                    common_subsequences = [substr]

                elif len(common_subsequences[0]) == len(substr):
                    common_subsequences += [substr]

    return sorted(list(set(common_subsequences)))


def main() -> int:
    n, *data = list(map(str.strip, sys.stdin))

    for i in range(0, int(n) * 2, 2):
        s1, s2 = data[i: i + 2]

        result = longest_subsequence(s1, s2)

        if not result:
            result = ['No Common Sequence Found']

        print('\n'.join(result), end='\n\n')

    return 0


if __name__ == "__main__":
    main()