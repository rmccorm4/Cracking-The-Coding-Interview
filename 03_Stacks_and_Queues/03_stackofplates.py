'''
Stack of Plates: 
---
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
'''
class SetOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		# Initial list of one empty stack
		self.stacks = [[]]
		# Index to keep track of current stack
		self.cur_stack = 0
	
	def push(self, value):
		# If our current stack is full
		if len(self.stacks[self.cur_stack]) == self.capacity:
			# Create new stack
			self.stacks.append([])
			# Increment stack index
			self.cur_stack += 1

		self.stacks[self.cur_stack].append(value)
		
	def pop(self, index=self.cur_stack):
		if len(self.stacks[self.cur_stack]) == 0:
			return None
		# We're about to empty our current stack
		elif len(self.stacks[self.cur_stack]) == 1:
			# Decrement which stack we're on if > 0
			if self.cur_stack > 0:
				self.cur_stack -= 1
		
		return self.stacks[self.cur_stack].pop()

	def popAt(self, index):
		if len(self.stacks[index]) > 0:
			return self.pop(index=index)
		else:
			return None
