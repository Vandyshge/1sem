import turtle

turtle.shape('turtle')
		
def sq(n):
	turtle.penup()
	turtle.left(180)
	turtle.forward(5)
	turtle.left(90)
	turtle.forward(5)
	turtle.left(90)
	turtle.pendown()
	for j in range(4):
		turtle.forward(n)
		turtle.left(90)

n = 10
for i in range(10):
	sq(n)
	n += 10
