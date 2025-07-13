# -*- coding: UTF-8 -*-
import random as r
import turtle as t
t.hideturtle()
t.speed(0)
t.bgcolor("green")
num = t.textinput("poker", "Enter your poker hand: ")
num = int(num)
pen = []
pens = []
nums = list(range(2,15))
cards = r.sample(nums,num)
x1 = -500
y1 = 200
for i in range(num):
    d = t.Turtle()
    d.card = cards[i]
    t.register_shape('cards/{}.gif'.format(str(d.card)))
    d.shape('cards/{}.gif'.format(str(d.card)))
    d.up()
    d.goto(x1,y1)
    pen.append(d)
    x1 += 139

newcard = []
for d in pen:
    for i in range(len(newcard)-1,-1,-1):
        key = newcard[i]
        x = key.xcor() + 139
        d.goto(x,0)
        if d.card > key.card:
            key.fd(139)
        else:
            d.goto(x, -200)
            newcard.insert(i+1, d)
            break
    else:
        d.goto(-500, -200)
        newcard.insert(0, d)

newcard = []
for d in pen:
    for i in range(len(newcard)-1,-1,-1):
        key = newcard[i]
        x = key.xcor() + 139
        d.goto(x,0)
        if d.card < key.card:
            key.fd(139)
        else:
            d.goto(x, -200)
            newcard.insert(i+1, d)
            break
    else:
        d.goto(-500, -200)
        newcard.insert(0, d)

t.done()