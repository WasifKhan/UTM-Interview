class LinkedList:
    def __init__(self, head=None):
        self.head = head

    @classmethod
    def from_range(cls, start, end):
        if start > end:
            return cls()
        current_node = ListNode(start)
        rest_of_the_list = cls.from_range(start+1, end)
        current_node.next = rest_of_the_list.head
        rest_of_the_list.head = current_node
        return rest_of_the_list

    def __str__(self):
        if self.head:
            return f"<{self.head}>"
        else:
            return "<>"

    def remove(self, value):
        if not self.head:
            pass
        elif self.head.value == value:
            self.head = self.head.next
        else:
            self.head._remove(value)

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next:
            return f"{self.value}, {self.next}"
        else:
            return str(self.value)

    def _remove(self, value):
        if not self.next:
            pass
        elif self.next.value == value:
            self.next = self.next.next
        else:
            self.next._remove(value)

# from_range example
# my_list = LinkedList.from_range(1,4)
# print(my_list)
# my_list = LinkedList.from_range(4,1)
# print(my_list)
# my_list = LinkedList.from_range(4,100)
# print(my_list)

# remove example
# my_list = LinkedList.from_range(1,4)
# print(my_list)
# my_list.remove(99)
# print(my_list)
# my_list.remove(3)
# print(my_list)
# my_list.remove(1)
# print(my_list)
# my_list.remove(4)
# print(my_list)
# my_list.remove(2)
# print(my_list)

# reverse example
# my_list = LinkedList.from_range(1,4)
# print(my_list)
# my_list.reverse()
# print(my_list)
