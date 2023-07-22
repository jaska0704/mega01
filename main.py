# import turtle
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)

# def drawSquare(a):
#     for i in range(4):
#         move(a)

# def drawColor(a, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     drawSquare(a)
#     turtle.end_fill()

# turtle.speed(1)

# drawColor(40, 'red')
# turtle.goto(100, 100)
# drawColor(60, "blue")
# turtle.goto(-150,-150)
# drawColor(80, 'red')
# turtle.goto(-150,150)
# drawColor(100, 'orange')
# turtle.goto(150,-150)
# drawColor(120, 'green')
def xpn(a:int, b:int):
    sum = 0
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            sum += 1
    return sum
print(xpn(12, 12))