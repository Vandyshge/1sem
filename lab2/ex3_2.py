# from random import randint
import turtle as t


# number_of_turtles = 5
# steps_of_time_number = 100


# pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
# for unit in pool:
#     unit.penup()
#     unit.speed(50)
#     unit.goto(randint(-200, 200), randint(-200, 200))


# for i in range(steps_of_time_number):
#     for unit in pool:
#         unit.forward(2)


def Trance(x0, y0, Vx, Vy, ay, n, dt):
	t.shape('turtle')
	t.penup()
	x, y = x0, y0
	Vx, Vy = Vx, Vy
	for i in range(n):
		t.goto(x, y)
		x += Vx * dt
		dy = Vy * dt + ay * dt ** 2 / 2
		
		Vy += ay * dt

Trance(0, 0, 0, 50, -10, 1000, 0.01)
