class Post(object):
	def __init__ (self,text):
		self.text = text
class User(object):
	def __init__ (self,name,email,password):
		self.name = name 
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []

	def add_friend(self,email):
		print(self.name + " has added " + email + " as a friend ")
		self.friends_list.append(email)

	def remove_friend(self,email):
		print(self.name + " has removed " + email)
		self.friends_list.remove(email)

	def post(self,text):
		post1 = Post(text)
		print(self.name + " has posted " + text )

	def get_userInfo(self):
		print(" name " + self.name + " email " + self.email + " password " + self.password + " friends " + str (self.friends_list) + " posts " + str (self.posts) )

	def comment(self,comment) :
		print ( self.name + " has commented on your post " )

user1 = User( " ghida " , " ghida15@yahoo.com " , " 100200300ghida " )
user2 = User( " jessica " , " jess2004@yahoo.com " , " thisismine " )
user1.add_friend( " jess2004@yahoo.com " )
user2.post( " Life is beautiful Be Happy !!! ")
user1.comment(" that's true " )
user1.get_userInfo()
user2.get_userInfo()
user1.remove_friend( " jess2004@yahoo.com " )

global_list=[]

def users():
	A = input( " what is your name ? " )
	B = input( " what is your email ? " )
	C = input( " what is your password ? " )
	user3 = ( A , B , C )
	global_list.append( user3 )

def posts():
	W = input( " what is your name ? " )
	X = input( " what is your email ? " )
	Y = input( " what is your password ? " )
	Z = input( " what is your text ? " )
	user4 = ( W , X , Y , Z )
	global_list.append( user4 )
	
class Comment(Post):
	def __init__ (self,like,reply):
		Post.__init__(self)
		self.like = like
		self.reply = reply
