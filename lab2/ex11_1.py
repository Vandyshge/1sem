import turtle as t

def lep(a):
	for i in range(360):
		t.left(1)
		t.forward(a)
	for i in range(360):
		t.right(1)
		t.forward(a)


def ex10(n):
	t.speed(3)
	t.right(90)
	a = 1
	for i in range(1, 10):
		lep(a)
		a += 1

ex10(2)