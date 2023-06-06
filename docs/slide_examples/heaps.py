class MinHeap:
    def __init__(self):
        self._heap = []

    def __str__(self):
        return str(self._heap)

    def _is_valid_index(self, index):
        if 0 <= index and index < len(self._heap):
            return True
        return False

    def push(self, value):
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def _sift_up(self, index):
        parent_index = (index-1) // 2
        if self._is_valid_index(parent_index) and self._heap[index] < self._heap[parent_index]:
            self._swap_nodes(index, parent_index)
            self._sift_up(parent_index)

    def _swap_nodes(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def pop_min(self):
        if not self._heap:
            raise IndexError("Tried to pop an empty MinHeap")
        self._swap_nodes(0, -1)
        min_value = self._heap.pop()
        self._sift_down(0)
        return min_value

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

    @classmethod
    def from_list(cls, lst):
        min_heap = cls()
        min_heap._heap = lst
        if min_heap._is_valid():
            return min_heap
        return None

    def _is_valid(self):
        for index in range(1, len(self._heap)):
            parent_index = (index-1) // 2
            if self._heap[index] < self._heap[parent_index]:
                return False
        return True

    @classmethod
    def heapify(cls, lst):
        min_heap = cls()
        min_heap._heap = lst
        min_heap._heapify()
        return min_heap

    def _heapify(self):
        for index in reversed(range(len(self._heap))):
            self._sift_down(index)


def kth_smallest(lst, k):
    min_heap = MinHeap.heapify(lst)
    try:
        for _ in range(k):
            min_value = min_heap.pop_min()
    except IndexError:
        raise IndexError("kth smallest value doesn't exist")
    return min_value


# push example
# min_heap = MinHeap()
# min_heap.push(7)
# min_heap.push(6)
# min_heap.push(5)
# min_heap.push(4)
# min_heap.push(3)
# min_heap.push(2)
# min_heap.push(1)
# print(min_heap)

# pop_min example
# min_heap = MinHeap()
# min_heap.push(4)
# min_heap.push(2)
# min_heap.push(1)
# print(min_heap)
# print(min_heap.pop_min())
# print(min_heap.pop_min())
# print(min_heap.pop_min())
# print(min_heap)
# 
# try:
#     min_heap.pop_min()
# except IndexError as e:
#     print(e)

# from_list example
# min_heap = MinHeap.from_list([1, 2, 3, 4, 5, 6, 7])
# print(min_heap)
# min_heap = MinHeap.from_list([7, 6, 5, 4, 3, 2, 1])
# print(min_heap)

# heapify example
# min_heap = MinHeap.heapify([7, 6, 5, 4, 3, 2, 1])
# print(min_heap)
# min_heap = MinHeap.heapify([5, 15, 35, 40, -5, 20, 0])
# print(min_heap)

# kth_smallest example
# print(kth_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# print(kth_smallest([9, 8, 7, 6, 5, 4, 3, 2, 1], 3))
# print(kth_smallest([-5, 0, 5, 10, 15, 20, 25], 1))
# print(kth_smallest([-5, 0, 5, 10, 15, 20, 25], 5))
# try:
#     kth_smallest([], 1)
# except IndexError as e:
#     print(e)
