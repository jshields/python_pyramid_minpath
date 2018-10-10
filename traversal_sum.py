import sys

"""
Leetcode 120. Triangle
https://leetcode.com/problems/triangle/description/

Description of dynamic programming solution:
https://discuss.leetcode.com/topic/1669/dp-solution-for-triangle

Verification tool:
https://www.dcode.fr/path-search-pyramid-triangle
"""


def load_rows_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        rows = []
        for row_index, line in enumerate(data):
            ints_row = [int(value) for value in line.split()]
            rows.append(ints_row)
        return rows


def min_path_cost(triangle):
    """
    :param triangle: a triangle of cost values,
        such that the each cost node has two children,
        starting from a single root
    :type triangle: lst[lst[int]]
    :return: minimum path cost/sum
    :rtype: int
    """
    # TODOC: writeup on space / time complexity. Shoudl be O(n), O(n^2) respectively?
    n = len(triangle)

    # copy the last row (which has no children to find the min for)
    # we only need a single row for holding the accumulated sum values for each step
    # the row will start as the last row in the triangle
    # (the children that the second to last row will pick the min from)
    minpath = triangle[-1]

    # step backwards from the second to last row, until we reach the top row
    # add the min path length up to the parent, so the answer is built cumulatively
    # until we reach the top, where the total min path cost sum is stored.
    # this makes the algorithm "bottom up"

    for i in range(n - 2, -1, -1):  # NOTE: -2 because it's zero indexed and the last row doesn't have children
        for j in range(i + 1):  # +1 because the row below is 1 longer
            # accumulate the sum from the left or right child,
            # whichever has the min path, onto the value of the current parent node,
            # and store that in `minpath` for the process to be repeated
            minpath[j] = triangle[i][j] + min(minpath[j], minpath[j + 1])

    # To put it another way:
    # The top of the triangle has now had the min of its children added to it,
    # and the min of its children have each had the min of its children added to it,
    # and so forth.
    # Therefore the root value is now equal to the solution.
    return minpath[0]


if __name__ == '__main__':
    # running from command line, not being imported
    if len(sys.argv) == 1:  # only .py file name was supplied as arg
        raise ValueError('No pyramid txt file supplied')
    else:
        filename = sys.argv[1]
        triangle = load_rows_from_file(filename)
        print(min_path_cost(triangle))
