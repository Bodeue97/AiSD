from random import random
from typing import Any, Callable, List
from random import randrange





class BinaryNode:
    def __init__(self, value:Any):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None
        self.parent: BinaryNode = None

    def __str__(self):
        return str(self.value)

    def level_of(self):
        lvl = 0
        parent = self.parent
        while parent != None:
            lvl += 1
            parent = parent.parent

        return lvl

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    def min(self):
        if not self.left_child :
            return self
        self.left_child.min()







class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value:Any):
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self._insert(self.root, value)

    def set_parents(self):
        root = self.root
        q = []
        q.append(root)
        if root == None:
            raise ValueError("khkhkh")
        while q:

            node = q[-1]

            del q[-1]
            if node.left_child:
                node.left_child.parent = node
                q.append(node.left_child)
            if node.right_child:
                node.right_child.parent=node
                q.append(node.right_child)




    def _insert(self, node:BinaryNode, value:Any):

            if value < node.value:
                if node.left_child:
                    self._insert(node.left_child, value)
                if not node.left_child:
                    node.left_child = BinaryNode(value)
                    node.left_child.parent = node
            if value > node.value:
                if node.right_child:
                    self._insert(node.right_child, value)
                if not node.right_child:
                    node.right_child = BinaryNode(value)
                    node.right_child.parent = node



    def remove(self, value:Any):
        if self.root.value != value
        self._remove(self.root, value)



    def _remove(self, node:BinaryNode, value: Any):
        if value == node.value:
            if node.is_leaf() is True:
                node = None
            if node.right_child:






    def insertList(self, list: List[Any]):
        for value in list:
            if not self.root:
                self.root = BinaryNode(value)
            else:
                self._insert(self.root, value)
    def contains(self, value: Any):
        if type(self) is BinarySearchTree:
            if not self.root:
                raise ValueError("Root = None")
            if self.root:
                node = self.root
                if value == node.value:
                    return True
                if value < node.value:
                    if not node.left_child:
                        return False
                    return BinarySearchTree.contains(node.left_child, value)
                if value > node.value:
                    if not node.right_child:
                        return False
                    return BinarySearchTree.contains(node.right_child, value)
        if type(self) is BinaryNode:
            if value == self.value:
                return True
            if value < self.value:
                if not self.left_child:
                    return False
                return BinarySearchTree.contains(self.left_child, value)
            if value > self.value:
                if not self.right_child:
                    return False
                return BinarySearchTree.contains(self.right_child, value)
    def show(self):

        spacer = " |===|"

        if type(self) is BinarySearchTree:
            if self.root is None:
                return
            if self.root.left_child:
                BinarySearchTree.show(self.root.left_child)
            print("|"+str(self.root.value)+"|")
            if self.root.right_child:
                BinarySearchTree.show(self.root.right_child)
        if type(self) is BinaryNode:
            if self.left_child:
                BinarySearchTree.show(self.left_child)

            print("  " + spacer*self.level_of()+str(self.value)+"|")
            if self.right_child:
                BinarySearchTree.show(self.right_child)















bst = BinarySearchTree()

arr = []
for x in range(10):
    arr.append(randrange(100))
# for x in arr:
    # bst.insert(x)
bst.insertList(arr)
print(bst.contains(50))



bst.show()

bst.set_parents()

bst.remove(10)