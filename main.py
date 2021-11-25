import typing
from typing import Any, List


class TreeNode:
    def __init__(self, value:Any):
        self.value = value
        self.children = []

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child : 'TreeNode'):
        self.children.append(child)









class Tree:
    def __init__(self, root: TreeNode):
        self.root = root


tn = TreeNode(1)
print(tn.is_leaf())
tn.add(TreeNode(2))
print(tn.is_leaf())
# print(tn.children[0].value)
