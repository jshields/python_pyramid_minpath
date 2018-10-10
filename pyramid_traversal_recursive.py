import sys

"""
Verification tool:
https://www.dcode.fr/path-search-pyramid-triangle


Solution based on:
http://www.csegeek.com/csegeek/view/tutorials/algorithms/trees/tree_part5.php


This program tries to summon the correct answer from the recursive depths,
but hangs on larger triangles.

At each step of the min path sum algorithm,
given the current selected node,
recurse on two more pyramids/trees using the left and right nodes as new root nodes,
finding the min path sum for each of the pyramids/trees.
At the lowest recursive depth, individual node values will be compared.
The lower sum between the left and right trees will be kept at each depth of recursion,
bubbling up the total min path sum to the top call.
"""

DEBUG = False


class NullNodeException(Exception):
    pass


class Node(object):

    def __init__(self, cost):
        self.cost = cost
        self.left = None
        self.right = None

    def __str__(self):
        return '{cost:02d}'.format(cost=self.cost)

    def __repr__(self):
        return '<Node {val}>'.format(val=str(self.cost))


class Pyramid(object):
    """
    This is really a binary tree but I wanted to make the py_ramid pun
    """

    def __init__(self, rows):
        """
        :param rows lst: 2D jagged list containing Node objects to populate the pyramid
        """
        self.root = rows[0][0]

        # `rows` is transient data because it would be "cheating" to use it later
        # (once the tree has been constructed, it should go away)
        # then, we will always access the tree via `root`
        self._link_nodes(rows)

        if DEBUG:
            if len(rows[0]) != 1:
                raise ValueError('Pyramid must have a pointy top')

            if self.root.left != rows[1][0] or self.root.right != rows[1][1]:
                raise ValueError('Root was not properly linked')

            self._init_pretty_print(rows)

    def _link_nodes(self, rows):

        rows_len = len(rows)
        for i in range(rows_len):

            # if not 2nd to last row (last row doesn't have children)
            if i < (rows_len - 1):
                cols_len = len(rows[i])
                if DEBUG:
                    if len(rows[i + 1]) != (cols_len + 1):
                        raise ValueError('Each row should be one node longer than the last')

                for j in range(cols_len):
                    node = rows[i][j]
                    node.left, node.right = self._adjacent_below(rows, i, j)

    def _get_node(self, rows, row_index, col_index):
        try:
            return rows[row_index][col_index]
        except IndexError:
            raise NullNodeException(
                'No node at row {row_index}, col {col_index})'.format(
                    row_index=row_index, col_index=col_index
                )
            )

    def _adjacent_below(self, rows, row_index, col_index):
        target_row_index = row_index + 1

        try:
            # the node below but in the same column appears to be the "left node"
            # when the pyramid / tree is pretty printed
            # (a 2D jagged array is being visualized as a binary tree)
            left_node = self._get_node(rows, target_row_index, col_index)
        except NullNodeException:
            left_node = None

        try:
            right_node = self._get_node(rows, target_row_index, col_index + 1)
        except NullNodeException:
            right_node = None

        return (left_node, right_node)

    def _init_pretty_print(self, rows):
        """
        This is based on static file data
        and *not* the actual node structure,
        therefore it could be misleading if something has gone wrong with
        linking the nodes.
        TODO Writing some more tests could help verify that won't happen.
        """
        self._pretty_pyramid = ''
        separator_unit = '  '
        num_rows = len(rows)
        for index, row in enumerate(rows):
            padding = (num_rows - index) * separator_unit
            row_str = separator_unit.join([str(node) for node in row])
            self._pretty_pyramid += '{pad}{row}\n'.format(pad=padding, row=row_str)

    def pretty_print(self):
        if DEBUG:
            print(self._pretty_pyramid)
        else:
            raise ValueError('No pretty triangles outside DEBUG mode')

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as file:
            data = file.readlines()
            rows = []
            for row_index, line in enumerate(data):
                nodes_row = [Node(int(value)) for value in line.split()]
                rows.append(nodes_row)

            return cls(rows)

    @classmethod
    def min_path_cost(cls, start_node):
        """
        The recursive approach works for smaller triangles,
        but chokes on large_triangle.txt
        """

        if start_node is None:
            return 0

        cost_sum = start_node.cost

        left_sum = cls.min_path_cost(start_node.left)
        right_sum = cls.min_path_cost(start_node.right)

        if left_sum <= right_sum:
            cost_sum += left_sum
        else:
            cost_sum += right_sum

        return cost_sum


if __name__ == '__main__':
    # running from command line, not being imported
    if len(sys.argv) == 1:  # only .py file name was supplied as arg
        raise ValueError('No pyramid txt file supplied')
    else:
        filename = sys.argv[1]
        pyramid = Pyramid.load_from_file(filename)
        if DEBUG:
            pyramid.pretty_print()
            print('Loaded pyramid')
            print('Calculating min path cost...')
        # we just give the minimum cost as the answer, not the actual path
        print(Pyramid.min_path_cost(pyramid.root))
