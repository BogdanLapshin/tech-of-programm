from random import randint, randrange

class VerificationIndicators:
	def __init__(self, consumers, tariff):
		self.averageСonsumption = 0
		self.consumers = consumers
		self.tariff = tariff

	# Посчитать сколько должна квартира по тарифам
	# Это сумма произвидения значения потребление и услуги
	# balance = потребление_газа * тариф_газа + ... + потребление_холодной воды * тариф_холодной воды
	def computeBalance(self, candidate):
		balance = 0
		for indicator, value in candidate['indicators'].items():
			balance += value * self.tariff[indicator]
		return balance

	# Невозможно програмно узнать правильно ли считает счетчик услуги
	# Но это можно имитировать
	# Предположим, что проверку не могут пройти те потребители
	# Услугой которой пользуются меньше чем, возможно, чтобы выжить
	# И наоборот, слишком много, чем если бы мы не выключали плиту, газ, свет 24/7
	# Тогда если значение одного из счетчиков неправильно, то
	# Верификация не пройдена и считается среднее потребление за все услуги
	# Так как предпологается, что и на других показателях значения неправильны
	def verification(self, candidate):
		for indicator, value in candidate['indicators'].items():
			if value < 10 or value > 100000:
				return False
		return True

	# Поэтому среднее потребление считается
	# Как среднее потребление всех квартир за все услуги
	def getAverageСonsumption(self):
		return sum([self.computeBalance(candidate) for candidate in self.consumers]) / len(self.consumers)

	# Проверка всех счетчиков во всех квартирах
	# Если проверка прошла, то считается потреблние
	# В ином случае считается среднее потребление за все услуги
	def verificationAll(self):
		currentAverageConsumption = self.getAverageСonsumption()
		for consumer in self.consumers:
			if self.verification(consumer):
				consumer['balance'] += self.computeBalance(consumer)
			else:
				consumer['balance'] += currentAverageConsumption

	# Данные потребителей за месяц
	def mounthDataShow(self, mounth):
		print('2020.1.{}'.format(mounth))
		for consumer in self.consumers:
			print('  Room №{}'.format(consumer['roomNumber']))
			print('    Consume:')
			print('       gas:         {} m^3'.format(consumer['indicators']['gas']))
			print('       cold water:  {} m^3'.format(consumer['indicators']['coldWater']))
			print('       hot water:   {} m^3'.format(consumer['indicators']['hotWater']))
			print('       electricity: {} KWatt * hour'.format(consumer['indicators']['electricity']))
			print('    Balance: {}'.format(consumer['balance']))
			print()
		self.setRandomConsumeData()


	# Имитируем потребление за месяц
	# И добросовесных людей, оплачивающие услуги
	# (идеальные условия)
	def setRandomConsumeData(self):
		curConsumers = []
		for consumer in self.consumers:
			curConsumer = consumer
			for indicator in consumer['indicators']:
				value = consumer['indicators'][indicator]
				curConsumer['indicators'][indicator] = max(10, randint(value - 20, value + 20))
				curConsumer['balance'] = 0
			curConsumers.append(curConsumer)
		self.consumers = curConsumers

dormTariff = {
	"gas": 9,
	"coldWater": 13,
	"hotWater": 97,
	"electricity": 0.144
}

dormConsumers = []
for roomNumber in range(1, 3):
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
	dormConsumers.append(curConsumer)

dorm = VerificationIndicators(dormConsumers, dormTariff)
for mounth in range(1, 13):
	dorm.mounthDataShow(mounth)
	dorm.verificationAll()
