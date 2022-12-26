#  File: OfficeSpace.py

#  Description: Returns the contested space, total space, and the uncontested space for each employee

#  Student Name: Preston Cook

#  Student UT EID: plc886

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: N/A

#  Date Created: 12/23/2022

#  Date Last Modified: 12/23/2022

import sys
from itertools import chain

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    x1, y1, x2, y2 = rect
    w = x2 - x1
    h = y2 - y1

    return w * h

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    flattened_matrix = list(chain(*bldg))
    return flattened_matrix.count(0)

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    flattened_matrix = list(chain(*bldg))

    cs = 0

    for num in flattened_matrix:
        if num >= 2:
            cs += 1
    
    return cs

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    uncont_space = 0

    x1, y1, x2, y2 = rect
    for i in range(y2 - y1):
            for j in range(x2 - x1):
                if bldg[i + y1 -1][j + x1 - 1] == 1:
                    uncont_space += 1
    
    return uncont_space

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    x1, y1, x2, y2 = office
    grid = []
    
    for _ in range(y2 - y1):
        arr = []
        for _ in range(x2 - x1):
            arr.append(0)
        grid.append(arr)
    
    for x1, y1, x2, y2 in cubicles:
        for i in range(y2 - y1):
            for j in range(x2 - x1):
                grid[i + y1 -1][j + x1 - 1] += 1
    return grid



# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
    w, h = map(int, sys.stdin.readline().split())
    office = (0, 0, w, h)
    requests = {}

    n = int(sys.stdin.readline())

    for _ in range(n):
        pieces = sys.stdin.readline().split()
        coords = tuple(map(int, pieces[1:]))
        requests[pieces[0]] = coords
    
    bldg = request_space(office, requests.values())
    us = unallocated_space(bldg)
    cs = contested_space(bldg)

    # print the following results after computation
    total = area(office)


    # compute the total office space
    print(f'Total {total}')

    # compute the total unallocated space
    print(f'Unallocated {us}')

    # compute the total contested space
    print(f'Contested {cs}')

    for k, v  in requests.items():
        print(f'{k} {uncontested_space(bldg, v)}')

    # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()