import turtle as t

def lep():
	for i in range(360):
		t.left(1)
		t.forward(1)
	for i in range(360):
		t.right(1)
		t.forward(1)


def ex10(n):
	t.speed(3)
	for i in range(n):
		lep()
		t.left(360 / n)

ex10(3)
