from turtle import *

def tree(branchLen):
  if branchLen > 5:
    forward(branchLen)
    right(20)
    tree(branchLen-15)
    left(40)
    tree(branchLen-15)
    right(20)
    backward(branchLen)
   
myWin = Screen()
left(90)
up()
backward(100)
down()
color('green')
tree(75)
myWin.exitonclick()
