class Node:

    def __init__(self, key, left=None, right=None): 
        self.left = left
        self.right = right
        self.key = key
    
    def insert(self, key):
        next_level = [self]
        while next_level:
            current_level = next_level
            next_level = []
            for node in current_level:
                if not node.left:
                    node.left = Node(key)
                    return
                elif not node.right:
                    node.right = Node(key)
                    return
                else:
                    next_level.append(node.left)
                    next_level.append(node.right)
