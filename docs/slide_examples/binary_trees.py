class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node
    
    def binary_search(self, value):
        if self.root_node:
            return self.root_node._binary_search(value)
        return False

    def insert_into_BST(self, value):
        if not self.root_node:
            self.root_node = TreeNode(value)
        else:
            self.root_node._insert_into_BST(value)

    def __str__(self):
        root = self.root_node if self.root_node else ''
        return f'<{root}>'

    def copy(self):
        new_root = self.root_node._copy() if self.root_node else None
        return Tree(new_root)

    def disconnect(self):
        if self.root_node:
            self.root_node._disconnect()

    def validate_BST(self):
        if not self.root_node:
            return True
        return self.root_node._validate_BST(None, None)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def _binary_search(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left._binary_search(value)
        elif value > self.value and self.right:
            return self.right._binary_search(value)
        else:
            return False

    def _insert_into_BST(self, value):
        if value <= self.value:
            if self.left:
                self.left._insert_into_BST(value)
            else:
                self.left = TreeNode(value)
        else:
            if self.right:
                self.right._insert_into_BST(value)
            else:
                self.right = TreeNode(value)

    def __str__(self):
        left = f'{self.left}, ' if self.left else ''
        right = f', {self.right}' if self.right else ''
        return f'{left}{self.value}{right}'

    def _copy(self):
        new_node = TreeNode(self.value)
        new_node.left = self.left._copy() if self.left else None
        new_node.right = self.right._copy() if self.right else None
        return new_node

    def _disconnect(self):
        if self.left:
            self.left._disconnect()
        if self.right:
            self.right._disconnect()
        self.left = None
        self.right = None

    def _validate_BST(self, lower_bound, upper_bound):
        if lower_bound != None and self.value <= lower_bound:
            return False
        elif upper_bound != None and node.value >= upper_bound:
            return False
        else:
            left_valid = self.left._validate_BST(lower_bound, self.value) if self.left else True
            right_valid = self.right._validate_BST(self.value, upper_bound) if self.right else True
            return left_valid and right_valid

# tree = Tree()
# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# tree.root_node = node2
# node2.left = node1
# node2.right = node3

# print(tree.binary_search(1))
# print(tree.binary_search(2))
# print(tree.binary_search(3))
# print(tree.binary_search(4))
# print(tree.binary_search(5))

# tree = Tree()
# tree.insert_into_BST(4)
# tree.insert_into_BST(2)
# tree.insert_into_BST(6)
# tree.insert_into_BST(1)
# tree.insert_into_BST(3)
# tree.insert_into_BST(5)
# tree.insert_into_BST(7)

# tree2 = tree.copy
# tree2 = tree
# print(tree)
# print(tree2)
# print(tree is tree2)



