import turtle as t

def lep():
	for i in range(180):
		t.right(1)
		t.forward(0.5)
	for i in range(180):
		t.right(1)
		t.forward(0.05)


def ex12(n):
	t.speed(3)
	t.left(90)
	for i in range(n):
		lep()

ex12(2)
