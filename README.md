python_pyramid_minpath
=======

(PyRamid)

Dynamic Programming Solution
----------------------------

Example usage:

    python3 traversal.py triangles/small_triangle.txt

    python3 traversal.py triangles/large_triangle.txt


This solution takes a bottom-up approach, adding minimum path values
starting with the bottom nodes and building on those stored values
as the program traverses up each row,
choosing the minimum value of the two children for each node.
In this way, the previously visited rows of the tree are "collapsed" into a single
accumulator row.



Recursive Solution
------------------

Alternate solution using recursion that chokes on large triangles:

    python3 pyramid_traversal_recursive.py triangles/small_triangle.txt


Running tests for alternate solution:

    python3 test_recursive_traversal_small_triangle.py


One reason this doesn't work well: Overlapping subtrees are still fully explored by the recursive calls
