def ug(n, a):
	f = 180 * (n - 2) / n

	turtle.left(180 - f / 2)

	for i in range(n):
		turtle.forward(a)
		turtle.left(180 - f)

	turtle.right(180 - f / 2)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()


import turtle

for i in range(3, 7):
	ug(i, 10 * i)
