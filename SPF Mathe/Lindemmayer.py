from gturtle import*
import random

def drawPath(startPosition, path, rightAngleRange, leftAngleRange, length):
    stack = [getPos()]
    setPos(startPosition[0], startPosition[1])
    for char in path:
        if char == "+":
            right(random.uniform(rightAngleRange[0], rightAngleRange[1]))
        elif char == "-":
            left(random.uniform(leftAngleRange[0], leftAngleRange[1])
        elif char == "[":
            

