def sp(a):
	import turtle

	turtle.shape('turtle')

	turtle.speed(1000)

	n = 0.001 * a
	for i in range(1000):
		turtle.forward(n)
		turtle.left(1)
		n += 0.001 * a

sp(1)
