from gturtle import *
from random import uniform

makeTurtle()
hideTurtle()
setPos(-390,150)
def drawpath(path,leftangle,rightangle,randangle,length,randlength):
    stack = [getPos()]
    heading(90) # turtle heads to the right
    for c in path:
        if c == "+":
            right(rightangle*uniform(1-randangle,1+randangle))
        elif c == "-":
            left(leftangle*uniform(1-randangle,1+randangle))
        elif c == "[":
            stack.append(getPos())
            stack.append(heading())
        elif c == "]":
            heading(stack.pop())
            setPos(stack.pop())
        else: # any other letter like "F"
            forward(length*uniform(1-randlength,1+randlength))
def lindenmayer(start,substitutions,leftangle,rightangle,randangle,length,randlength,steps):
    curve = start
    repeat steps:
        for s in substitutions:
            curve = curve.replace(s[0],s[1].lower())
        curve = curve.upper()
    drawpath(curve,leftangle,rightangle,randangle,length,randlength)
lindenmayer("F",[["F","F[+F][F--F+F-F+[F-F+FFF-F++F]]"]], 20, 16, 0.35, 20, 0, 4)