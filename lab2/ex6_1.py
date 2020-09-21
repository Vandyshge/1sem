def leg():
	turtle.forward(50)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(50)
	turtle.left(180)

def ex6(n):
	turtle.shape('turtle')
	for i in range(n):
		leg()
		turtle.left(360 / n)

import turtle

ex6(12)
