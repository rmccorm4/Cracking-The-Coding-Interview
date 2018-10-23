'''
Queue via Stacks:
---
Implement a MyQueue class which implements a queue using two stacks.
'''
class MyQueue:
	def __init__(self):
		# This will keep our pushed values, and put them onto
		# the pop stack periodically
		self.stack1 = []
		# This will keep track of our values to pop in order
		self.stack2 = []

	def enqueue(self, value):
		self.stack1.append(value)

	def dequeue(self):
		if len(self.stack2) > 0:
			return self.stack2.pop()

		elif len(self.stack2) == 0 and len(self.stack1) > 0:
			while len(self.stack1) > 1:
				self.stack2.append(self.stack1.pop())
			
			return self.stack1.pop()

		elif len(self.stack2) == 0 and len(self.stack1) == 0:
			return None

	def __str__(self):
		return str(self.stack2) + ' ' + str(list(reversed(self.stack1)))

if __name__ == '__main__':
	q = MyQueue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)
	print(q)
	print(q.dequeue())
	print(q)
	print(q.dequeue())
	print(q)
	print(q.dequeue())
	print(q)
	print(q.dequeue())
	print(q)
	print(q.dequeue())
	print(q)

