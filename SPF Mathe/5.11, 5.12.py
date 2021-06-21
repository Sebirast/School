from gturtle import *


def drawPath(path, angle, length):
    for c in path:
        if c == "+":
            rt(angle)
        elif c == "-":
            lt(angle)
        else:
            forward(length)


def main():
    path = "F-F" # for koch-snwoflake F++F++F,
    makeTurtle()
    hideTurtle()

    for i in range(4):
        path = path.replace("F","F-F++F-F")

    drawPath(path, 60, 1)


if __name__ == "__main__":
    main()