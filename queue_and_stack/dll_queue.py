# Check FAQ if import doesn't work
import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return
        else :
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
