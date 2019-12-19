import sys
sys.path.append('./dll_queue')
sys.path.append('./dll_stack')
sys.path.append('./doubly_linked_list')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    '''pseudocode:
    if insertion point found:
        create new node
    if value to insert < current node:
        go left
    else:
        go right
    '''
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        # parent = None
        # current = self
        # print('current: ', current)
        # while current != None:
            # if value < current.value:
                # print('in left branch')
                # parent = current
                # current = current.left
            # else:
                # print('right branch')
                # current = current.right
        # print('current after while: ', current)
        # current = BinarySearchTree(value)
        # parent.left = current
        # print('current value should be bst value: ', current.value, 'left: ', current.left, 'right: ', current.right)

    # Return True if the tree contains the value
    # False if it does not
    # searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else: 
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    # returns the maximum value in the binary search tree.
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # performs a traversal of _every_ node in the tree,
    # executing the passed-in callback function on each tree node value. 
    # There is a myriad of ways to perform tree traversal; in this case any of them should work. 
    def for_each(self, cb):
        stack = Stack()
        stack.push(self)
        print('self in for_each',self)
        while stack.len() > 0:

            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current = stack.pop()
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

myBST = BinarySearchTree(5)
# print(myBST.value, myBST.left)
myBST.insert(6)
myBST.insert(2)
myBST.insert(3)
myBST.insert(7)
print(myBST.in_order_print())
# print(myBST.value, myBST.right)
# print('Should be 3,6: ', myBST.left.right.value, myBST.right.left.value)