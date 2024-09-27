class Stack:

    def __init__(self, items=None, limit=100):
        # Initialize the stack with optional items and a capacity limit
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the stack if it's not full
        if not self.full():
            self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack if it's not empty, else None
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        # Return the top item without removing it, or None if the stack is empty
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        # Return the current size of the stack
        return len(self.items)

    def full(self):
        # Return True if the stack is full, otherwise False
        return len(self.items) >= self.limit

    def search(self, target):
        # Return the position of target in the stack, or -1 if not found
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        return -1