class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head_node = None

    def push(self, value):
        new_head = ListNode(value)
        new_head.next = self.head_node
        self.head_node = new_head

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next
            return value
        else:
            raise IndexError

    def peek(self):
        if self.head_node:
            return self.head_node.value
        else:
            raise IndexError

    def empty(self):
        if self.head_node:
            return False
        return True

# class Stack:
#     def __init__(self):
#         self.array = []
# 
#     def push(self, value):
#         self.array.append(value)
# 
#     def peek(self):
#         if self.array:
#             return self.array[-1]
#         else:
#             raise IndexError
# 
#     def pop(self):
#         if self.array:
#             return self.array.pop()
#         else:
#             raise IndexError
# 
#     def empty(self):
#         if self.array:
#             return False
#         return True

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print( stack.pop() )
# print( stack.pop() )
# print( stack.pop() )

def validate_enclosures(string):
    stack = Stack()
    for char in string:
        if char in ["(","[","{"]:
            stack.push(char)
        else:
            if stack.empty():
                return False
            matching_char = stack.pop()
            if char == ")":
                if matching_char != "(":
                    return False
            elif char == "]":
                if matching_char != "[":
                    return False
            elif char == "}":
                if matching_char != "{":
                    return False
            else:
                return False
    if stack.empty():
        return True
    return False

# string = "()"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)
# string = "[[[]]]"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)
# string = "()[]{}()[]{}"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)
# string = "(([](){}()[]))"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)
# string = "(()"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)
# string = "())"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)
# string = "({)}"
# return_value = validate_enclosures(string)
# print(string)
# print(return_value)

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, value):
        if self.min_stack.empty() or value <= self.min_stack.peek():
            self.min_stack.push(value)
        self.stack.push(value)

    def pop(self):
        if self.stack.peek() == self.min_stack.peek():
            self.min_stack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def peek_min(self):
        return self.min_stack.peek()

# min_stack = MinStack()
# min_stack.push(4)
# min_stack.push(5)
# print( min_stack.peek_min() )
# print( min_stack.peek() )
# min_stack.push(1)
# min_stack.push(2)
# print( min_stack.peek_min() )
# print( min_stack.peek() )
# min_stack.pop()
# min_stack.pop()
# print( min_stack.peek_min() )
# print( min_stack.peek() )

# class Queue:
#     def __init__(self):
#         self.head_node = None
#         self.tail_node = None

#     def enqueue(self, value):
#         new_node = ListNode(value)
#         if not self.tail_node:
#             self.head_node = new_node
#             self.tail_node = new_node
#         else:
#             self.tail_node.next = new_node
#             self.tail_node = new_node

#     def dequeue(self):
#         if not self.head_node:
#             raise IndexError
#         value = self.head_node.value
#         self.head_node = self.head_node.next
#         if not self.head_node:
#             self.tail_node = None
#         return value

#     def empty(self):
#         if self.head_node:
#             return False
#         return True

class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def enqueue(self, value):
        while not self.left_stack.empty():
            self.right_stack.push( self.left_stack.pop() )
        self.right_stack.push(value)

    def dequeue(self):
        while not self.right_stack.empty():
            self.left_stack.push( self.right_stack.pop() )
        return self.left_stack.pop()

    def empty(self):
        if self.left_stack.empty() and self.right_stack.empty():
            return True
        return False

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print( queue.dequeue() )
# print( queue.dequeue() )
# print( queue.dequeue() )


def reverse_queue(queue):
    stack = Stack()
    while not queue.empty():
        stack.push( queue.dequeue() )
    while not stack.empty():
        queue.enqueue( stack.pop() )

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# reverse_queue(queue)
# print( queue.dequeue() )
# print( queue.dequeue() )
# print( queue.dequeue() )

