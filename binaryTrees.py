# Binary Tree explorations


# Node structure for nodes in Tree
class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.value = val

# Tree structure, implements adding nodes to Tree and Removing Nodes.
# Supports printing in pre, post, and in order
class Tree:
  def __init__(self):
    self.root = None

  def getRoot(self):
    return self.root

  def add(self, val):
    if self.root is None:
      self.root = Node(val)
    else:
      # root of tree exists so we will use a different function to add nodes to tree
      self._add(val, self.root)

  def _add(self, val, node):
    if (val <= node.value): # put this item on the left
      if node.left is None:
        node.left = Node(val)
      else:
        self._add(val, node.left)
    else:
      if node.right is None:
        node.right = Node(val)
      else:
        self._add(val, node.right)

  def inOrderPrint(self):
        self._inOrderPrint(self.root)

  def _inOrderPrint(self, node):
        if node is None:
            return

        self._inOrderPrint(node.left)

        print(node.value)

        self._inOrderPrint(node.right)

  def preOrderPrint(self):
        self._preOrderPrint(self.root)

  def _preOrderPrint(self, node):
        if node is None:
            return

        print(node.value)

        self._preOrderPrint(node.left)

        self._preOrderPrint(node.right)

  def postOrderPrint(self):
        self._postOrderPrint(self.root)

  def _postOrderPrint(self, node):
        if node is None:
            return

        self._postOrderPrint(node.left)

        self._postOrderPrint(node.right)

        print(node.value)

if __name__ == "__main__":
    tree = Tree()
    tree.add(5)
    tree.add(4)
    tree.add(3)
    tree.add(1)
    tree.add(6)
    tree.add(8)
    tree.add(9)

    print('In Order Print')
    tree.inOrderPrint()

    print('Pre Order Print')
    tree.preOrderPrint()

    print('Post Order Print')
    tree.postOrderPrint()
