import turtle
x=turtle.Turtle()
print('please give us size')
a=input()
try:
    a=int(a)
except ValueError:
    a=float(a)
print('please give us color')
b=input()
x.color(b)
x.begin_fill()
for i in range(4):
    x.forward(a)
    x.right(90)
x.end_fill()
turtle.done()