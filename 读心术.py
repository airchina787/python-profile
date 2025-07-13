import turtle as t

t.tracer(False)
t.bgcolor("green")
t.hideturtle()
t.up()
cards = []
for i in range(52):
    t.register_shape("poker/{}.gif".format(i))
    cards.append("poker/{}.gif".format(i))

n = 1
for i in range(6):
    x,y = -240,165
    t.clear()
    for card in cards:
        j = cards.index(card)
        if j % (2*n)>=n:
           t.goto(x,y)
           t.shape(card)
           t.stamp()
           x = x+80
           if x > 240:
               x = -240
               y = y-110
        
    key = t.textinput("询问","屏幕上有没有你的牌？（是/否）")
    n *=2
