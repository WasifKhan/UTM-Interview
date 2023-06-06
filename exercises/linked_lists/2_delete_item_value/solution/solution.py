class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def _delete_item_by_value(self, value):
        if not self.next:
            pass
        elif self.next.data != value:
            self.next._delete_item_by_value(value)
        elif self.next.next == None:
            self.next = None
        else:
            self.next = self.next.next


class linkedlist:

    def __init__(self, head=None):
        self.head = head
    
    def delete_item_by_value(self, value):
        if self.head == None:
            pass
        elif self.head.next == None:
            if self.head.data == value:
                self.head = None
        else:
            self.head._delete_item_by_value()
