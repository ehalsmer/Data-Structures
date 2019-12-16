# Check FAQ if import doesn't work
import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? Python lists are forbidden (we need not and may not use them)
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # should add an item to the back of the queue.
        pass

    def dequeue(self):
        # should remove and return an item from the front of the queue.
        pass

    def len(self):
        # returns the number of items in the queue.
        return self.storage.length
        # pass
