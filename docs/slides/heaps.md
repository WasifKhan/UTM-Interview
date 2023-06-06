<!-- .slide: data-state="title" -->

# Heaps

---

## Topics
- Introduction to Heaps
- Implementation
- Interview Problems

---

## Introduction to Heaps
- Definition
- Array Representation

---

## Definition
- A ***complete binary tree*** is a binary tree where every layer except the last is completely full
- The leaves in the last layer of a complete binary tree are as far left as possible

![complete binary tree](images/complete_binary_tree.png)
<!-- .element class="fragment" -->

---

## Definition
- A ***heap*** is a complete binary tree that satisfies a particular ordering
- There are two types of heap, a ***max heap*** and a ***min heap***
- For a min heap, the value of every node is smaller than the value of either child
- For a max heap, the value of every node is greater than the value of either child
- Either one of these constraints is called the ***heap property***

![heap](images/heap.png)
<!-- .element class="fragment" -->

---

## Array Representation
- Heaps can be represented as an array by mapping each node to an index
- The root of the heap is stored at index `0`
- The left child of a node at index `i` is stored at index `2*i + 1`
- The right child of a node at index `i` is stored at index `2*i + 2`
- The parent of a node at index `i` is stored at `(i-1) // 2`
- The array `[1, 3, 5, 4, 8, 9, 6]` corresponds to this min heap:

![heap](images/heap.png)
<!-- .element class="fragment" -->

---

## Implementation
- Min Heap
- Push
- Push Visualization
- Pop Min
- Pop Min Visualization

---

## Min Heap
- A min heap is an instance of the `MinHeap` class:
```
class MinHeap:
    def __init__(self):
        self._heap = []
    
    def __str__(self):
        return str(self._heap)
    
    def _is_valid_index(self, index):
        if 0 <= index and index < len(self._heap):
            return True
        return False
    
    def _swap_nodes(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]
```
- A Python list is used to represent the heap internally
- `_is_valid_index` is a helper method that checks whether a given index is in bounds
- `_swap_nodes` is a helper method that swaps two nodes

---

## Push
- <code class="code-info">Problem:</code> Implement the `MinHeap` method `push`
- `push` takes in a value to be inserted
- `push` inserts the value into the heap

---

## Push
- Append the value at the end of the array:
```
class MinHeap:
    def push(self, value):
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)
```
- The end of the array corresponds to the bottom of the tree
- This potentially violates the heap property
- Call the helper method `_sift_up` to restore the heap property

---

## Push
- Swap the inserted node with its parent if they violate the heap property
- Call `_sift_up` recursively on parent if the nodes were swapped:
```
class MinHeap:
    def _sift_up(self, index):
        parent_index = (index-1) // 2
        if self._is_valid_index(parent_index) and self._heap[index] < self._heap[parent_index]:
            self._swap_nodes(index, parent_index)
            self._sift_up(parent_index)
```
- The runtime of `push` is O(log(n))

---

## Push
- Running:
```
min_heap = MinHeap()
min_heap.push(7)
min_heap.push(6)
min_heap.push(5)
min_heap.push(4)
min_heap.push(3)
min_heap.push(2)
min_heap.push(1)
print(min_heap)
```
- Outputs:
```
[1, 4, 2, 7, 5, 6, 3]
```

---

## Push Visualization
- Push the value `1` to this min heap

![push heap 1](images/push_heap_1.png)
<!-- .element class="fragment" -->

---

## Push Visualization
- Append `1` to the bottom of the tree
- The heap property is now being violated

![push heap 2](images/push_heap_2.png)
<!-- .element class="fragment" -->

---

## Push Visualization
- Swap `1` with its parent `6` to restore the heap property
- The heap property is now being violated further up

![push heap 3](images/push_heap_3.png)
<!-- .element class="fragment" -->

---

## Push Visualization
- Swap `1` with its parent `2`
- The heap property is now restored everywhere
- `push` execution is complete

![push heap 4](images/push_heap_4.png)
<!-- .element class="fragment" -->

---

## Pop Min
- <code class="code-info">Problem:</code> Implement the `MinHeap` method `pop_min`
- `pop_min` removes the minimum value of the heap
- `pop_min` returns the value removed
- `pop_min` raises an `IndexError` if the heap is empty

---

## Pop Min
- In order to maintain the complete binary tree, only last element can be removed
- Swap the root with the last node, then remove:
```
class MinHeap:
    def pop_min(self):
        if not self._heap:
            raise IndexError("Tried to pop an empty MinHeap")
        self._swap_nodes(0, -1)
        min_value = self._heap.pop()
        self._sift_down(0)
        return min_value
```
- This potentially violates the heap property
- Call the helper method `_sift_down` to restore the heap property

---

## Pop Min
- Swap the root node with its smallest child if they violate the heap property
- Call `_sift_down` recursively on the child if the nodes were swapped:
```
    def _sift_down(self, index):
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2
        if self._is_valid_index(right_child_index):
            if self._heap[left_child_index] < self._heap[right_child_index]:
                smallest_child_index = left_child_index
            else:
                smallest_child_index = right_child_index
        elif self._is_valid_index(left_child_index):
            smallest_child_index = left_child_index
        else:
            return
        if self._heap[smallest_child_index] < self._heap[index]:
            self._swap_nodes(smallest_child_index, index)
            self._sift_down(smallest_child_index)
        return
```
- This function is complex because there are three different cases:
- A node can have two children, one child, or zero children
- The runtime of `pop_min` is O(log(n))

---

## Pop Min
- Running:
```
min_heap = MinHeap()
min_heap.push(4)
min_heap.push(2)
min_heap.push(1)
print(min_heap)
print(min_heap.pop_min())
print(min_heap.pop_min())
print(min_heap.pop_min())
print(min_heap)
try:
    min_heap.pop_min()
except IndexError as e:
    print(e)
```
- Outputs:
```
[1, 4, 2]
1
2
4
[]
Tried to pop an empty MinHeap
```

---

## Pop Min Visualization
- Pop the minimum value from this min heap

![heap](images/heap.png)
<!-- .element class="fragment" -->

---

## Pop Min Visualization
- Swap the root node with the last node
- The heap property is now being violated

![pop heap 2](images/pop_heap_2.png)
<!-- .element class="fragment" -->

---

## Pop Min Visualization
- Remove the minimum, which is now in the last node

![pop heap 3](images/pop_heap_3.png)
<!-- .element class="fragment" -->

---

## Pop Min Visualization
- Swap `6` with its smallest child `3` to restore the heap property
- The heap property is now being violated further down

![pop heap 4](images/pop_heap_4.png)
<!-- .element class="fragment" -->

---

## Pop Min Visualization
- Swap `6` with its smallest child `4`
- The heap property is now restored everywhere
- `pop_min` execution is complete

![pop heap 5](images/pop_heap_5.png)
<!-- .element class="fragment" -->

---

## Interview Problems
- Heap from Valid List
- Heapify
- kth smallest element

---

## Heap from Valid List
- <code class="code-info">Problem:</code> Implement the `MinHeap` custom constructor `from_list`
- `from_list` takes in a Python list
- `from_list` checks if the list represents a valid heap
- If the input is a valid heap, `from_list` outputs a `MinHeap` representing the same heap
- If the input is not a valid heap, `from_list` outputs `None`

---

## Heap from Valid List
- Initialize heap from given list:
```
class MinHeap:
    @classmethod
    def from_list(cls, lst):
        min_heap = cls()
        min_heap._heap = lst
        if min_heap._is_valid():
            return min_heap
        return None
```
- Call the helper method `_is_valid` to check validity

---

## Heap from Valid List
- Iterate backwards over the list:
```
class MinHeap:
    def _is_valid(self):
        for index in range(1, len(self._heap)):
            parent_index = (index-1) // 2
            if self._heap[index] < self._heap[parent_index]:
                return False
        return True
```
- Check the heap property between every node and its parent
- The runtime of `from_list` is O(n)

---

## Heap from Valid List
- Running:
```
min_heap = MinHeap.from_list([1, 2, 3, 4, 5, 6, 7])
print(min_heap)
min_heap = MinHeap.from_list([7, 6, 5, 4, 3, 2, 1])
print(min_heap)
```
- Outputs:
```
[1, 2, 3, 4, 5, 6, 7]
None
```

---

## Heapify
- <code class="code-info">Problem:</code> Implement the `MinHeap` custom constructor `heapify`
- `heapify` takes in a Python list
- `heapify` constructs a valid heap from the elements in the list, reordering them if necessary
- `heapify` outputs a `MinHeap`

---

## Heapify
- Initialize heap from given list:
```
class MinHeap:
    @classmethod
    def heapify(cls, lst):
        min_heap = cls()
        min_heap._heap = lst
        min_heap._heapify()
        return min_heap
```
- Call the helper method `_heapify` to reorder elements into a valid heap

---

## Heapify
- Iterate backwards over the list:
```
class MinHeap:
    def _heapify(self):
        for index in reversed(range(len(self._heap))):
            self._sift_down(index)
```
- Call the `_sift_down` helper method on each element to move it to the correct location

---

## Heapify
- This is the same `_sift_down` helper that was used in the `pop_min` method:
```
    def _sift_down(self, index):
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2
        if self._is_valid_index(right_child_index):
            if self._heap[left_child_index] < self._heap[right_child_index]:
                smallest_child_index = left_child_index
            else:
                smallest_child_index = right_child_index
        elif self._is_valid_index(left_child_index):
            smallest_child_index = left_child_index
        else:
            return
        if self._heap[smallest_child_index] < self._heap[index]:
            self._swap_nodes(smallest_child_index, index)
            self._sift_down(smallest_child_index)
        return
```
- The runtime of `heapify` is O(n)

---

## Heapify
- Running:
```
min_heap = MinHeap.heapify([7, 6, 5, 4, 3, 2, 1])
print(min_heap)
min_heap = MinHeap.heapify([5, 15, 35, 40, -5, 20, 0])
print(min_heap)
```
- Outputs:
```
[1, 3, 2, 4, 6, 7, 5]
[-5, 5, 0, 40, 15, 20, 35]
```

---

## kth smallest element
- <code class="code-info">Problem:</code> Implement the function `kth_smallest`
- `kth_smallest` takes in a Python list and an integer k
- `kth_smallest` outputs the kth smallest value from the list
- `kth_smallest` raises an `IndexError` if called on a list with less than k elements

---

## kth smallest element
- Heapify the input list:
```
def kth_smallest(lst, k):
    min_heap = MinHeap.heapify(lst)
    try:
        for _ in range(k):
            min_value = min_heap.pop_min()
    except IndexError:
        raise IndexError("kth smallest value doesn't exist")
    return min_value
```
- Call `pop_min` k times
- The runtime of `kth_smallest` is O(k\*log(n))

---

## kth smallest element
- Running:
```
print(kth_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(kth_smallest([9, 8, 7, 6, 5, 4, 3, 2, 1], 3))
print(kth_smallest([-5, 0, 5, 10, 15, 20, 25], 1))
print(kth_smallest([-5, 0, 5, 10, 15, 20, 25], 5))
try:
    kth_smallest([], 1)
except IndexError as e:
    print(e)
```
- Outputs:
```
3
3
-5
15
kth smallest value doesn't exist
```

---

<!-- .slide: data-state="title" -->

# End of 
# Heaps

