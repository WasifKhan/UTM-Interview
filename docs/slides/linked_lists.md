<!-- .slide: data-state="title" -->

# Linked Lists

---

## Topics
- Introduction to Linked Lists
- Processing Linked Lists
- Interview Problems

---

## Introduction to Linked Lists
- Definition
- Visualization
- Implementation

---

## Definition
- <code class="code-warning">Reminder:</code> Linked lists are not related to Python lists
- Python lists are implemented as dynamic arrays
- It is important to differentiate between the two clearly
- In today's lecture, only linked lists will be talked about

---

## Definition
- A linked list is a ***recursive data structure***
- Recursive data structures are partially composed of simpler instances of themselves
- Just like recursive functions, recursive data structures need a simple, non-recursive base case

---

## Definition
- A ***linked list*** is either:
- 1) Empty
- or 
- 2) A value and a reference to another linked list

---

## Visualization
- A linked list can be conceptualized as a chain
- An individual link in the chain is called a ***list node***
- The first link in the chain is called a ***head node***
- The whole chain reachable from the head node is called a linked list

![linked list](images/linked_list.png)
<!-- .element class="fragment" -->

---

## Implementation
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

## Implementation
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

## Implementation
- Python is not aware of the relationship between list nodes
- The programmer creates and maintains the references between nodes manually

---

## Processing Linked Lists
- Create Linked List from Integer Range
- Print Linked List
- Delete a Node from a Linked List

---

## Create Linked List from Integer Range
- <code class="code-info">Problem:</code> Implement the `LinkedList` custom constructor `from_range`
- `from_range` takes in two integers, a start of a range and an end
- `from_range` outputs a linked list containing all the integers in the range between start and end
- The head node should contain the starting integer, the rest of the nodes should be in order

---

## Create Linked List from Integer Range
- Create one node at a time, and use a recursive call to process the rest:
```
class LinkedList:
    @classmethod
    def from_range(cls, start, end):
        if start > end:
            return cls()
        current_node = ListNode(start)
        rest_of_the_list = cls.from_range(start+1, end)
        current_node.next = rest_of_the_list.head
        rest_of_the_list.head = current_node
        return rest_of_the_list
```
- `from_range` is implemented as a class method
- The runtime of this method is O(n)

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

## Delete a Node from a Linked List
- <code class="code-info">Problem:</code> Implement the `LinkedList` method `remove`
- `remove` takes in a value to be deleted
- `remove` deletes the first node with the corresponding value from the linked list
- If the next node is to be deleted, the reference from the current node should be changed to skip it

![delete node](images/delete_node.png)
<!-- .element class="fragment" -->

---

## Delete a Node from a Linked List
- Check whether the head is deleted in the `LinkedList` method:
```
class LinkedList:
    def remove(self, value):
        if not self.head:
            pass
        elif self.head.value == value:
            self.head = self.head.next
        else:
            self.head._remove(value)
```
- Implement the `_remove` helper method in the `ListNode` class to process the recursion

---

## Delete a Node from a Linked List
- Recurse until the next node is the one to be deleted:
```
class ListNode:
    def _remove(self, value):
        if not self.next:
            pass
        elif self.next.value == value:
            self.next = self.next.next
        else:
            self.next._remove(value)
```
- There are two base cases: one when the end of the list is reached
- The other is when the next value is to be deleted
- The runtime of this method is O(n)

---

## Interview Problems
- Reverse a Linked List

---

## Reverse a Linked List
- <code class="code-info">Problem:</code> Implement the `LinkedList` method `reverse`
- `reverse` reverses the linked list

---

## Reverse a Linked List
- Iterate through the list while reversing the reference to the next node at each step
```
class LinkedList:
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
```
- The method needs to maintain references to the previous, current, and next node at each step
- There are four lines of code executed at each iteration of the while loop
- One line reverses the current node's internal reference to the next node
- The other three lines update the function's references to the previous, current, and next node
- The runtime of this method is O(n)

---

<!-- .slide: data-state="title" -->

# End of 
# Linked Lists

