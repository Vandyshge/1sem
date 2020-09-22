from random import *
import turtle as t

def Trance():
	t.left(randint(0, 360))
	t.forward(randint(-100, 100))

for i in range(10):
	Trance()
