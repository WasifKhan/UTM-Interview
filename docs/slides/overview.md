<!-- .slide: data-state="title" -->

# Stacks and Queues

## Storing Information for Effective Processing

---

## Topics
- Linked List Recap
- Stack Data Structure
- Exercise
- Queue Data Structure
- Exercise

---

## Linked List Recap - Definition
- A linked list is a ***recursive data structure***
- A ***linked list*** is either:
1) Empty
or 
2) A value and a reference to another linked list
- <code class="code-warning">Reminder:</code> Linked lists are not related to Python lists

---

## Linked List Recap - Visualization
- A linked list can be conceptualized as a chain
- An individual link in the chain is called a ***list node***
- The first link in the chain is called a ***head node***
- The whole chain reachable from the head node is called a linked list

![linked list](images/linked_list.png)
<!-- .element class="fragment" -->

---

## Linked List Recap - Implementation
- A linked list is an instance of the `LinkedList` class:
```
class LinkedList:
    def __init__(self, head=None):
        self.head = head
```
- A linked list only contains a reference to the head node
- An empty linked list had no head node
- The Python constant `None` is used to represent an absent head node

---

## Linked List Recap - Implementation
- A list node is an instance of the `ListNode` class:
```
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```
- The Python constant `None` is used when there is no next node
- This implementation deviates slightly from the mathematical definition

---

## Print Linked List
- Python doesn't know how to print a linked list
- <code class="code-info">Problem:</code> Implement the `LinkedList` dunder method `__str__`
- `__str__` outputs the values in the linked list in order, starting from the head node
- Angle brackets should be used to denote the start and end of the list
- Commas should be used to separate the values in the list

---

## Print Linked List
- Use the `__str__` method in the `LinkedList` class to output the outside angle brackets:
```
class LinkedList:
    def __str__(self):
        if self.head:
            return f"<{self.head}>"
        else:
            return "<>"
```
- Converting `self.head` to a string calls the `__str__` dunder method in the `ListNode` class

---

## Print Linked List
- Use the `__str__` dunder method in the `ListNode` class to process the recursion:
```
class ListNode:
    def __str__(self):
        if self.next:
            return f"{self.value}, {self.next}"
        else:
            return str(self.value)
```
- The recursive call is hidden, it happens when `self.next` is converted to a string
- The runtime of this method is O(n)

---

## Stack Data Structure
- Definition
- Visualization
- Implementation

---

## Definition
- A stack is a data structure that organizes elements in a particular order
- A stack supports two main operations: `push`, and `pop`
- `push` adds a data value to the stack, `pop` removes a data value from the stack
- The order that elements are stored is: Last In First Out (LIFO)
- The last value that is pushed onto the stack, is the first one that is popped off the stack

---

## Visualization
- A stack can be conceptualized as a stack of plates
- The push operation puts a plate on top of the stack
- The pop operation takes a plate from the top of the stack
- Taking plates off the top, and putting them back on top preserves LIFO order
- The last plate put on top is the first one picked up later

![stack](images/stack.png)
<!-- .element class="fragment" -->

---

## Implementation
- A stack is implemented using a linked list:
```
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
```
- `push` adds a data value to the stack in O(1) time
- `pop` removes a data value from the stack and returns it in O(1) time
- Calling `pop` on an empty stack causes an `IndexError` exception be raised

---

## Implementation
- Two more methods are defined for convenience:
```
class Stack:
    def peek(self):
        if self.head_node:
            return self.head_node.value
        else:
            raise IndexError
    
    def empty(self):
        if self.head_node:
            return False
        return True
```
- `empty` returns a boolean value: `True` if the stack is empty, and `False` if the stack contains data
- `peek` returns the top element of a stack without removing that element
- Calling `peek` on an empty stack causes an `IndexError` exception be raised

---

## Exercise
- Validate Enclosures

---

## Validate Enclosures
- <code class="code-info">Problem:</code> Write the function `validate_enclosures`
- `validate_enclosures` takes in a string consisting of these enclosures: `( ) [ ] { }`
- `validate_enclosures` returns `True` if all the enclosures are correctly balanced, `False` otherwise
- Use a stack for the solution
- Parse the string one character at a time
- Push opening enclosures onto a stack
- For closing enclosures, check for a matching opening enclosure on top of the stack

---

## Validate Enclosures
- Implementation:
```
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
```
- The runtime of `validate_enclosures` is O(n)

---

## Queue Data Structure
- Definition
- Visualization
- Implementation

---

## Definition
- A queue is a data structure that organizes elements in the opposite order of a stack
- A queue supports two main operations: `enqueue` and `dequeue`
- `enqueue` adds a data value to the queue, `dequeue` removes a data value from the queue
- The order that elements are kept in is: First In First Out (abbreviated FIFO)
- The first element in the queue, is the first element out of the queue

---

## Visualization
- A queue can be conceptualized as line at the store
- People get in at the back of the line, the person at the front of the line goes first
- `enqueue` puts a person at the back of the line
- `dequeue` removes a person from the front of the line
- This preserves FIFO order, the first person to get in line, is the first person to get out

![queue](images/queue.png)
<!-- .element class="fragment" -->

---

## Implementation
- A queue is implemented with a linked list
- This implementation defines three methods: `enqueue`, `dequeue`, and `empty`
- `empty` returns a boolean value corresponding to whether the queue is empty
- Calling `dequeue` on an empty queue causes an `IndexError` to be raised

---

## Implementation

- This is the linked list implementation:
```
class Queue:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node

    def dequeue(self):
        if not self.head_node:
            raise IndexError
        value = self.head_node.value
        self.head_node = self.head_node.next
        if not self.head_node:
            self.tail_node = None
        return value

    def empty(self):
        if self.head_node:
            return False
        return True
```

---

# Exercise
- Reverse a Queue

---

## Reverse a Queue
- This function takes in a queue and reverses it
- The strategy is to use a stack
- First, empty the queue onto the stack
- Then, empty the stack back onto the queue
- The LIFO ordering of the stack will reverse the order of all the elements

---

## Reverse a Queue
- This is the implementation:
```
def reverse_queue(queue):
    stack = Stack()
    while not queue.empty():
        stack.push( queue.dequeue() )
    while not stack.empty():
        queue.enqueue( stack.pop() )
```

---

<!-- .slide: data-state="title" -->

# End of
# Stacks and Queues
