def sp(a):
	turtle.forward(a)
	turtle.left(90)

def ex8(n, a0, b):
	turtle.shape('turtle')
	turtle.speed(1)
  
	a = a0
	for i in range(n):
		sp(a)
		a += b

import turtle

ex8(10, 5, 5)
