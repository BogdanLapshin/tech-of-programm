import unittest
from random import randrange
from main import VerificationIndicators

class TestDorm(unittest.TestCase):
	def setUp(self):

		self.dormTariff = {
			"gas": 9,
			"coldWater": 13,
			"hotWater": 97,
			"electricity": 0.144
		}

		self.dormConsumers = []
		self.countOfRooms = 26
		for roomNumber in range(1, self.countOfRooms):
			curConsumer = {
				'roomNumber': roomNumber,
				'indicators': {
					"gas": randrange(40, 100, 1),
					"coldWater": randrange(3000, 5000, 1),
					"hotWater": randrange(3000, 5000, 1),
					"electricity" : randrange(3000, 5000, 1)
				},
				'balance': 0
			}
			self.dormConsumers.append(curConsumer)

		self.dorm = VerificationIndicators(self.dormConsumers, self.dormTariff)

	# Значение тарифов должно быть не отрицательное число
	def test_limit_tariff(self):
		for tariff, value in self.dormTariff.items():
			if value <= 0:
				self.assertTrue(True, False) # Способ сказать, что тест не прошёл, потому что True != False
		self.assertTrue(True, True)
	
	def test_compute_balance(self):
		allBalancesTest = []
		allBalances = []
		for consumer in self.dormConsumers:
			balance = sum([value * self.dormTariff[indicator] for indicator, value in consumer['indicators'].items()])
			allBalancesTest.append(balance)
			allBalances.append(self.dorm.computeBalance(consumer))
		self.assertEqual(allBalances, allBalancesTest)

	def test_average_consumption(self):
		testAverage = 0
		for consumer in self.dormConsumers:
			testAverage += self.dorm.computeBalance(consumer)
		testAverage /= len(self.dormConsumers)
		self.assertEqual(testAverage, self.dorm.getAverageСonsumption())

if __name__ == '__main__':
	unittest.main()