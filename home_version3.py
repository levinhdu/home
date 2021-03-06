import turtle
import math
t = turtle.Turtle()
t.pensize(3)
turtle.bgcolor("skyblue")
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def hcn(d,r,mau):
    t.fillcolor(mau)
    t.begin_fill()
    for i in range(2):
        t.fd(d)
        t.lt(90)
        t.fd(r)
        t.lt(90)
    t.end_fill()
def tamgiaccan(h,goc,mau):
    t.fillcolor(mau)
    t.begin_fill()
    t.fd(h)
    t.lt(goc)
    t.fd(h*(math.sqrt(2)/2))
    t.lt(90)
    t.fd(h*(math.sqrt(2)/2))
    t.lt(goc)
    t.end_fill()
def hinhthang(d,h,goc,mau):
    t.fillcolor(mau)
    t.begin_fill()
    t.fd(d)
    t.lt(goc)
    c = h/math.sin(math.radians(180-goc))
    t.fd(c)
    t.lt(180-goc)
    t.fd(d-(math.cos(math.radians(180-goc))*c*2))
    t.lt(180-goc)
    t.fd(c)
    t.lt(100)
    t.end_fill()
def ongkhoi():
    move(-150, 100)
    t.fillcolor("orange")
    t.begin_fill()
    t.lt(135)
    t.fd(20)
    t.rt(45)
    t.fd(30)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(13)
    t.end_fill()
    move(-165, 180)
    t.fd(15)
    move(-180, 200)
    t.fd(30)
    t.lt(90)
move(-300,0)
hcn(200,100,"yellow")
move(-300,100)
tamgiaccan(150,135,"red")
move(-235,0)
hcn(30,60,"blue")
move(-170,50)
hcn(40,20,"blue")
hcn(40,10,"blue")
hcn(20,20,"")

ongkhoi()

move(150,100)
tamgiaccan(100,135,"green")
move(160,150)
tamgiaccan(80,135,"green")
move(170,190)
tamgiaccan(60,135,"green")
move(200,0)
t.bk(30)
hinhthang(60,100,100,"brown")

move(75,50)
tamgiaccan(50,135,"green")
move(80,75)
tamgiaccan(40,135,"green")
move(85,95)
tamgiaccan(30,135,"green")
move(90,0)
t.bk(5)
hinhthang(30,50,100,"brown")
turtle.done()

