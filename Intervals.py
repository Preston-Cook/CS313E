#  File: Intervals.py

#  Description: Merges tuples where intervals overlap

#  Student Name: Preston Cook

#  Student UT EID: plc886

#  Partner Name: N/A

#  Partner UT EID: plc886

#  Course Name: CS 313E

#  Unique Number: N/A

#  Date Created: 12/21/2022

#  Date Last Modified: 12/21/2022
import sys


def merge_tuples(tuples_list):
    sorted_tups = sorted(map(list, tuples_list))
    stack = [sorted_tups[0]]

    for interval in sorted_tups[1:]:
        if stack[-1][0] <= interval[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], interval[-1])
        else:
            stack.append(interval)

    return list(map(tuple, stack))


def sort_by_interval_size(tuples_list):
    return sorted(tuples_list, key=lambda x: x[0] - x[1], reverse=True)


def test_cases():
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    # write your own test cases

    assert sort_by_interval_size([(1, 3), (4, 5)]) == [(4, 5), (1, 3)]
    # write your own test cases

    assert merge_tuples([(1, 4), (3, 9)]) == [(1, 9)]

    return "all test cases passed"


def main():
    n = int(sys.stdin.readline())

    intervals = []

    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        p1, p2 = map(int, line.split())
        intervals.append((p1, p2))

    merged_tups = merge_tuples(intervals)

    sorted_tups = sort_by_interval_size(merged_tups)

    print(merged_tups, sorted_tups, sep='\n')


if __name__ == "__main__":
    main()
