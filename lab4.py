from turtle import Turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle.__init__(self)
		self.r = r/10
		self.dx=dx
		self.dy=dy
		self.shape("circle")
		self.penup()
		self.color(color)
	def move(self,screen_width,screen_height):
		fx = food.xcor()

b =Ball(5,"yellow", 4,5)