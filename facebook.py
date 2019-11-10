class User(object):
	def __init__ (self,name,email,password):
		self.name = name 
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []
	def add_friend(self,email):
		print(self.name + " has added " + self.email + " as a friend ")
		self.friends_list.append(email)
	def remove_friend(self,email):
		print(self.name + " has removed " + self.email)
		self.friends_list.remove(email)
	def post(self,text):
		self.text=text
		print(self.name + " has posted " + self.text )