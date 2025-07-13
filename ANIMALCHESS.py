import turtle as t
import random as r
import time as m
chess = ["cat","rat","dog","wolf","leopard","tiger","lion","elephant"]
pwd = []
for i in range(4):
    pwd.append(r.choice(chess))
chess.sort()
t.speed(0)
t.setup(800,600)
t.pensize(2)
t.hideturtle()
t.bgcolor("lightblue")
y = 150
for f in chess:
    t.register_shape("animal_chess/{}.gif".format(f))

for row in range(4):
    t.penup()
    t.goto(-360,y - 40)
    t.pd()
    for i in range(4):
        t.fd(80)
        t.lt(90)

    x = -240
    animals = []
    for f in chess:
        tur = t.Turtle()
        tur.shape("animal_chess/{}.gif".format(f))
        tur.up()
        tur.goto(x, y)
        animals.append(tur)
        x += 80
    y -= 100
    l, r = 0, 7
    while True:
        mid = (l + r) // 2
        animals[mid].backward(mid * 80 + 80)
        if mid > chess.index(pwd[row]):
            t.bgcolor("red")
            m.sleep(1)
            r =mid - 1
            animals[mid].fd(mid * 80 + 80)
            t.bgcolor("lightblue")
        elif mid < chess.index(pwd[row]):
            t.bgcolor("green")
            m.sleep(0.5)
            l = mid+1
            animals[mid].fd(l * 80 + 80)
            t.bgcolor("lightblue")
        else:
            t.bgcolor("gold")
            m.sleep(0.5)
            t.bgcolor("lightblue")
            break

t.done()
