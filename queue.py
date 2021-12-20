class Node:
	def __init__(self, val=None, prevNode=None, nextNode=None):
		self.val = val
		self.nextNode = nextNode
		self.prevNode = prevNode

class Queue:
	def __init__(self):
		self.head = self.tail = None

	def enqueue(self, data):
		newNode = Node(data)
		if self.head:
			newNode.prevNode = self.tail
			self.tail.nextNode = newNode
		else:
			self.head = newNode
		self.tail = newNode

	def pop(self):
		res = self.tail.val
		if self.size() == 1:
			self.head = self.tail = None
		else:
			self.tail = self.tail.prevNode
			self.tail.nextNode = None
		return res

	def front(self):
		return self.tail.val

	def back(self):
		return self.head.val

	def size(self):
		size = 0
		newNode = self.head
		while newNode:
			size += 1
			newNode = newNode.nextNode
		return size

	def isEmpty(self):
		if self.size() == 0:
			return True
		return False

	def show(self):
		display = []
		newNode = self.head
		while newNode:
			display.append(newNode.val)
			newNode = newNode.nextNode
		return display

if __name__ == "__main__":
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output="test-reports")