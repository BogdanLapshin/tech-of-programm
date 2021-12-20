import unittest
from random import randint
from queue import Queue, Node

class TestQueue(unittest.TestCase):
	def setUp(self):
		self.queue = Queue()
		self.testq = []
		self.n = randint(10, 20)

	def test_enqueue(self):
		for i in range(self.n):
			self.queue.enqueue(i)
			self.testq += [i]
		self.assertEqual(self.queue.show(), self.testq)

	def test_dequeue(self):
		for i in range(self.n):
			self.queue.enqueue(i)
			self.testq += [i]
		for i in range(self.n // 2):
			self.queue.pop()
			self.testq.pop()
		self.assertEqual(self.queue.show(), self.testq)

	def test_isEmpty(self):
		self.assertEqual(self.queue.isEmpty(), True)

	def test_isNotEmpty(self):
		self.queue.enqueue(1)
		self.assertEqual(self.queue.isEmpty(), False)

	def test_size(self):
		for i in range(self.n):
			self.queue.enqueue(i)
		self.assertEqual(self.queue.size(), self.n)

	def test_front(self):
		randomNumber = randint(123, 12345)
		for i in range(self.n):
			self.queue.enqueue(i)
		self.queue.enqueue(randomNumber)
		self.assertEqual(self.queue.front(), randomNumber)

	def test_back(self):
		randomNumber = randint(123, 12345)
		self.queue.enqueue(randomNumber)
		for i in range(self.n):
			self.queue.enqueue(i)
		self.assertEqual(self.queue.back(), randomNumber)

if __name__ == '__main__':
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output="test-reports")
	unittest.main(testRunner=runner)
	unittest.main()