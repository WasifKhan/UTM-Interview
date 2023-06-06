class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def _delete_end(self):
        if self.next.next == None:
            self.next = None
        else:
            self.next._delete_end()


class linkedlist:

    def __init__(self, head = None):
        self.head = head
    
    def delete_end(self):
        if self.head == None:
            pass
        elif self.head.next == None:
            self.head = None
        else:
            self.head._delete_end()
        