import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value and self.left:
                return self.left.contains(target)
            elif target > self.value and self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # BFT Steps:
        # initialize a queue
        q = Queue()
        # push root to queue
        q.enqueue(node)
        # while stack not empty
        while q.size > 0:
            # pop top item out of queue into temp
            current_node = q.dequeue()
            # DO THE THING!!!!!!
            if current_node:
                print(current_node.value)
            # if temp has right right put into queue
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)
            # if temp has left left put into queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # DFT Steps:
        # initialize a stack
        s = Stack()
        # push root to stack
        s.push(node)
        # while stack not empty
        while s.size > 0:
            # pop top item out of stack into temp
            current_node = s.pop()
            # DO THE THING!!!!!!
            if current_node:
                print(current_node.value)
            # if temp has right right put into stack
            if current_node.left:
                s.push(current_node.left)
            if current_node.right:
                s.push(current_node.right)
            # if temp has left left put into stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
