'''
Stack Min
---
How would you design a stack which, in addition to push and pop, has a
function min() which returns the minimum element? push(), pop(), and
min() should all operate in O(1) time.
'''
class MinStack:
    def __init__(self):
        # Keep track of values as they're added
        self.val_stack = []
        # Keep track of minimums as we encounter them
        self.min_stack = []

    def top(self):
        if len(self.val_stack) > 0:
            return self.val_stack[-1]
        else:
            return None
        
    def push(self, value):
        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        self.val_stack.append(value)

    def pop(self):
        if len(self.val_stack) > 0:
            retval = self.val_stack.pop()
        else:
            return None

        if retval == self.min_stack[-1]:
            # update min if we are removing it from stack
            self.min_stack.pop()
        return retval

    def getMin(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None

