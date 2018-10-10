import sys
from copy import deepcopy

"""
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


def min_path_magic(triangle):
    """
    Bottom up

    :param triangle: a triangle of cost values,
        such that the each cost node has two children,
        starting from a single root
    :type triangle: lst[lst[int]]
    :return: minimum path
    :rtype: lst[lst[int]] containing sums up to that point in the path
    """
    n = len(triangle)  # n = number of rows

    # dynamic programming  approach stores results so far in this data structure, building up to the solution,
    # shaped like the original triangle
    # but contains min sums up to that point in the path
    # triangle is a literal square cut in half:
    # about O(n^2 / 2), actual number of nodes for rows n is the "Triangular number"
    # https://en.wikipedia.org/wiki/Triangular_number
    # Asymptotic Notation space complexity: O(n^2)
    divine = deepcopy(triangle)  # FIXME: no nested items, `[x for x in triangle]` may be faster?

    # step backwards from the second to last row, until we reach the top row
    # NOTE: -2 because it's zero indexed and the last row doesn't have children
    for i in range(n - 2, -1, -1):

        for j in range(i + 1):
            target_child_row = i + 1

            divine[i][j] = triangle[i][j] + min(
                divine[target_child_row][j],  # left child
                divine[target_child_row][j + 1]  # right child
            )

    return divine


def path_to_enlightenment(truth_triangle):
    """
    Top down

    :param truth_triangle: the truth triangle contains the real node values
    """

    # the divination triangle points the way down the min path
    divination_triangle = min_path_magic(truth_triangle)

    # follow the guidance of the divination triangle,
    # down the path to enlightenment on the triangle of truth
    n = len(truth_triangle)

    # now go down a pretend triangle the size of both
    # truth triangle and divination triangle
    # keep track of which node we're on so we compare the correct children

    node = truth_triangle[0][0]
    path = [node]  # path starts at root node

    # we traverse down 1 row each time but only increment column if going right
    node_col = 0
    for node_row in range(n - 1):  # -1 to skip last row (no children)

        target_child_row = node_row + 1

        left = divination_triangle[target_child_row][node_col]
        right = divination_triangle[target_child_row][node_col + 1]

        # traverse according to divination triangle,
        # add the node from truth triangle to the path
        if (left < right):
            # go left
            node = truth_triangle[target_child_row][node_col]
            # move down one row with no col change = "left"
        else:
            # go right
            node = truth_triangle[target_child_row][node_col + 1]
            node_col += 1

        path.append(node)

    return path


if __name__ == '__main__':
    # running from command line, not being imported
    if len(sys.argv) == 1:  # only .py file name was supplied as arg
        raise ValueError('No pyramid txt file supplied')
    else:
        filename = sys.argv[1]
        truth_triangle = load_rows_from_file(filename)

        for node in path_to_enlightenment(truth_triangle):
            print(node)
