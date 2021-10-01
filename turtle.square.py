#Drawing a square using turtle
import turtle
n = int(input())
m = int(input())
for i in range(8):
    if(i%2==0):
        print(i)
        turtle.forward(n)
        turtle.left(m)
