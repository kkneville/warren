# a game of bunnies

import random

class Warren(object):
	def __init__(self, name, residence, chief):
		self.name = name
		self.residence = residence
		self.chief = chief
		self.capacity = 100
		self.owsla = []
		self.rabbits = []
		self.log = []
		self.hunger = 10
		self.health = 10
		self.state = "rest"

	def count(self):
		count = 0
		for rabbit in rabbits:
			count += 1
		for member in owsla:
			count += 1
		return count
	
	def log(self, type, num=0, name1="", name2=""):
		if type = "birth":
			log.push("{} kits were born to {} and {}".format(num, name1, name2))


# name generator			


class Rabbit(object):
	def __init__(self, mother, father):
		self.name = "none"
		self.age = "kit"
		self.markings = "none"

	def nameGen(self):
		suffix = ["heart", "tail", "ear", "foot", "paw", "run", "star", "tree", "bloom", "meadow", "thorn", "berry"]
		prefix = ["bramble", "holly", "rose", "elm", "ash","hazel", "merry", "mouse", "flora", "birch", "sorrel", "water", "rain", "winter", "snow", "sun", "mountain", "valley"]
		name = "{} {}".format(prefix[random.randint(0, len(suffix))], suffix[random.randint(0, len(suffix))] )


	def eat(self, num):
		self.hunger += 1*num
		return self

	def graze(self):
		if self.hunger == 10
			return self
		self.hunger += 1
			return self		

	def sleep(self):
		self.state = "sleep"
		return self


			
