import kdtree

emptyTree = kdtree.create(dimensions=3)

point1 = (2, 3, 4)
point2 = [4, 5, 6]

import collections
Point = collections.namedtuple('Point', 'x y z')
tree = kdtree.create([point1, point2, point3])
tree.add( (5, 4, 3) )
tree = tree.remove( (5, 4, 3) )
list(tree.inorder())
list(kdtree.level_order(tree))
tree.search_nn( (1, 2, 3))
tree.add( (10, 2, 1) )
subtree = tree.right
tree.right = None
tree.right = subtree
tree.is_balanced
tree.is_balanced
tree = tree.rebalance()
tree.is_balanced