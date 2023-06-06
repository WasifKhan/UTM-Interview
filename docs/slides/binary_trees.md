<!-- .slide: data-state="title" -->

# Binary Trees

---

## Topics
- Introduction to Binary Trees
- Basic Functions
- Tree Traversals
- Tree Interview Problems

---

# Introduction to Binary Trees
- Binary Tree Definition
- Binary Tree Visualization
- Binary Search Trees
- Python Implementation

---

## Binary Tree Definition
- Binary Trees are a recursive data structure
- Binary Trees are either:
- 1) Empty
- 2) A binary tree node
- A binary tree node is a single data value, and two references
- A left reference to another binary tree node, and a right reference to another binary tree node

---

## Binary Tree Definition
- The binary tree node that references another binary tree node is called a parent node
- The binary tree node that is referenced by another binary tree node is called a child node
- The "binary" adjective refers to the fact that binary trees have two children, a left child and a right child
- This course only covers binary trees, but it is possible in general to have more than two children per node

---

## Binary Tree Visualization
- The node at the top of the tree with no parents is called a root node
- The nodes on the bottom with no children are called leaf nodes
- The depth of a node is the number of edges from the root node to it
- The height of a tree is the maximum depth of any leaf
- A tree that is part of a bigger tree is called a subtree

![binary tree](images/binary_tree.png)
<!-- .element class="fragment" -->

---

## Binary Search Trees
- A binary search tree (abbreviated BST) is a binary tree with two restrictions:
- The value in a node is greater than any value in the left subtree of that node
- The value in a node is less than any value in the right subtree of that node

![perfect binary search tree](images/perfect_binary_search_tree.png)
<!-- .element class="fragment" -->

---

## Python Implementation
- The Python constant `None` is used to represent an absent node
- The tree is implemented using a wrapper class:
```
class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node
```
- The nodes are implemented using a `TreeNode` class:    
```
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

---

# Basic Functions
- Binary Search
- Binary Search Runtime
- Insert a Node into a Binary Search Tree

---

## Binary Search
- Implement the `Tree` method `binary_search`
- This method should be called on a binary search tree
- This method takes in a value to search for
- It returns `True` if the value exists in the tree, `False` otherwise
- The strategy is very simple, this is what binary search trees are optimized for
- If the value we're looking for is smaller than the current node, go left
- If the value we're looking for is larger than the current node, go right

---

## Binary Search
- This is the implementation:
```
class Tree:
    def binary_search(self, value):
        if self.root_node:
            return self.root_node._binary_search(value)
        return False
```
```
class TreeNode:
    def _binary_search(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left._binary_search(value)
        elif value > self.value and self.right:
            return self.right._binary_search(value)
        else:
            return False
```

---

## Binary Search Runtime
- The worst case runtime of binary search is linear: O(n) where n is the number of nodes in the tree
- This happens in the case of degenerate binary trees
- A degenerate binary tree is a tree where every non-leaf node only has only one child
- Searching for the last element in a degenerate binary tree requires looking through every previous node
- Notice that a degenerate binary tree has the same structure as a linked list

![unbalanced binary search tree](images/unbalanced_binary_search_tree.png)
<!-- .element class="fragment" -->

---

## Binary Search Runtime
- In general, binary search is slower the deeper it has to look into the tree
- A degenerate tree has maximum possible height for its number of nodes, so the worst case run time is slower
- A perfect tree is a tree where all leaves are at the same depth
- A perfect tree has minimum possible height for its number of nodes, so the worst case run time isn't as bad

![perfect binary search tree](images/perfect_binary_search_tree.png)
<!-- .element class="fragment" -->

---

## Binary Search Runtime
- The worst case runtime of binary search is proportional to the height of the tree
- Every time the number of nodes in a perfect tree (approximately) doubles, the height only grows by 1
- This relationship is called logarithmic: h ~ log(n)
- Binary search only has to look at one node at every level of the tree
- Therefore, the worst case runtime of binary search on a perfect tree is logarithmic: O(log(n))

![perfect binary search tree](images/perfect_binary_search_tree.png)
<!-- .element class="fragment" -->
---

## Binary Search Runtime
- A tree doesn't have to be perfectly balanced for quick search
- It just can't be *too* lopsided
- The exact math of what counts as "balanced" is beyond the scope of this course
- Very balanced or very unbalanced trees should be intuitively obvious
- Searching a balanced tree is O(log(n))
- Searching an unbalanced tree is O(n)
- Modern databases use a tree structure to organize data
- They use complex strategies to keep the tree balanced, so that searching the database is quick

---

## Insert a Node into a Binary Search Tree
- Implement the `Tree` method `insert_into_BST`
- This method should be called on a BST
- It takes in a value to be inserted, and inserts a new node with that value
- To find the correct location, binary search for where it should go, then insert the new node as a leaf

---

## Insert a Node into a Binary Search Tree
- This is the implementation:
```
class Tree:
    def insert_into_BST(self, value):
        if not self.root_node:
            self.root_node = TreeNode(value)
        else:
            self.root_node._insert_into_BST(value)
```
```
class TreeNode:
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
```
- The runtime of this method is the same as binary search
- O(n) for unbalanced trees, O(log(n)) for balanced trees

---

## Insert a Node into a Binary Search Tree
- Inserting these values in this order:
```
tree = Tree()
tree.insert_into_BST(4)
tree.insert_into_BST(2)
tree.insert_into_BST(6)
tree.insert_into_BST(1)
tree.insert_into_BST(3)
tree.insert_into_BST(5)
tree.insert_into_BST(7)
```
- Produces this perfect tree:

![perfect binary search tree](images/perfect_binary_search_tree.png)
<!-- .element class="fragment" -->

---

## Insert a Node into a Binary Search Tree
- Inserting these values in this order:
```
tree = Tree()
tree.insert_into_BST(1)
tree.insert_into_BST(2)
tree.insert_into_BST(3)
tree.insert_into_BST(4)
```
- Produces this degenerate tree:

![unbalanced binary search tree](images/unbalanced_binary_search_tree.png)
<!-- .element class="fragment" -->

---

# Tree Traversals
- Types of Traversals
- Print Tree Inorder
- Copy Tree
- Delete Tree

---

## Types of Traversals
- A tree traversal is an algorithm that visits each node of a tree exactly once
- There is no one way to traverse a tree, there are many ways to order which nodes you visit first
- The three simplest traversal orderings are called: inorder, preorder, and postorder

---

## Types of Traversals
- Each order is defined recursively
- Inorder traversal follows this order:
- First, it goes down the left subtree
- Second, it visits the root
- Third, it goes down the right subtree
```
traverse_inorder(root_node):
    traverse_inorder(root_node.left)
    visit(root_node)
    traverse_inorder(root_node.right)
```

---

## Types of Traversals
- Preorder traversal follows this order:
- First, it visits the root
- Second, it goes down the left subtree
- Third, it goes down the right subtree
```
traverse_preorder(root_node):
    visit(root_node)
    traverse_preorder(root_node.left)
    traverse_preorder(root_node.right)
```

---

## Types of Traversals
- Postorder traversal follows this order:
- First, it goes down the left subtree
- Second, it goes down the right subtree
- Third, it visits the root
```
traverse_postorder(root_node):
    traverse_postorder(root_node.left)
    traverse_postorder(root_node.right)
    visit(root_node)
```

---

## Print Tree Inorder
- Implement print functionaly for a `Tree` using the `__str__` magic method
- The tree should print its elements comma-separated, between angle brackets
- The order of the values will be according to an inorder traversal
- For a BST, this order will be strictly increasing

---

## Print Tree Inorder
- This is the implementation:
```
class Tree:
    def __str__(self):
        root = self.root_node if self.root_node else ''
        return f'<{root}>'
```
```
class TreeNode:
    def __str__(self):
        left = f'{self.left}, ' if self.left else ''
        right = f', {self.right}' if self.right else ''
        return f'{left}{self.value}{right}'
```
- This method, like any simple inorder traversal, has a runtime of O(n)

---

## Copy Tree
- Implement the `Tree` method `copy`
- `copy` returns a copy of the tree it was called on

---

## Copy Tree
- Implementation:
```
class Tree:
    def copy(self):
        new_root = self.root_node._copy() if self.root_node else None
        return Tree(new_root)
```
```
class TreeNode:
    def _copy(self):
        new_node = TreeNode(self.value)
        new_node.left = self.left._copy() if self.left else None
        new_node.right = self.right._copy() if self.right else None
        return new_node
```
- This method, like any simple preorder traversal, has a runtime of O(n)

---

## Disconnect Tree
- Impelment the `Tree` method `disconnect`
- `disconnect` sets all left and right references in every node to `None`
- Once the connections are severed, a node can't access its children anymore
- A postorder traversal is necessary to do this

---

## Disconnect Tree
- Implementation:
```
class Tree:
    def disconnect(self):
        if self.root_node:
            self.root_node._disconnect()
```
```
class TreeNode:
    def _disconnect(self):
        if self.left:
            self.left._disconnect()
        if self.right:
            self.right._disconnect()
        self.left = None
        self.right = None
```
- This method, like any simple postorder traversal, has a runtime of O(n)

---

# Tree Interview Problems
- Validate a Binary Search Tree

---

## Validate a Binary Search Tree
- Implement the `Tree` method `validate_BST`
- `validate_BST` returns `True` if called on a BST, `False` otherwise
- The strategy is maintain a lower bound and an upper bound for permitted values
- The value in a node becomes an upper bound for its left subtree
- The value in a node becomes a lower bound for its right subtree

![perfect binary search tree](images/perfect_binary_search_tree.png)
<!-- .element class="fragment" -->

---

## Validate a Binary Search Tree
- Implementation:
```
class Tree:
    def validate_BST(self):
        if not self.root_node:
            return True
        return self.root_node._validate_BST(None, None)
```
```
class TreeNode:
    def _validate_BST(self, lower_bound, upper_bound):
        if lower_bound != None and self.value <= lower_bound:
            return False
        elif upper_bound != None and self.value >= upper_bound:
            return False
        else:
            left_valid = self.left._validate_BST(lower_bound, self.value) if self.left else True
            right_valid = self.right._validate_BST(self.value, upper_bound) if self.right else True
            return left_valid and right_valid
```
- Notice this is a preorder traversal, the current node is processed before the recursive calls

---

<!-- .slide: data-state="title" -->

# End of
# Binary Trees

