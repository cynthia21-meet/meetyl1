class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummy!!" + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self,sound):
		print(self.name + " says " + self.sound)*3
cat = Animal("miao","jenny","2","black")
cat.description()
cat.eat("bread")
cat.make_sound("miao")

class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self,breakfast):
		print(self.name + " is eating " + breakfast)
girl = Person(" cynthia "," 15 "," Beir ouna "," girl ")