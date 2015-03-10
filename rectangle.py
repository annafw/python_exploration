import turtle;
import random;

bob=turtle.Turtle();

def squareBob():
    for i in range(4):
        bob.fd(200)
        bob.rt(90)

def triangleBob(size=100):
    for i in range(3):
        bob.fd(size)
        bob.lt(120)

def circleBob(size=100):
    for i in range(360):
        bob.fd(3)
        bob.lt(1)

def spiral(side, angle, steps):
    if(steps > 0):  # when steps = 0 (or less than) stop
        bob.fd(side)
        bob.rt(angle)
        spiral(side+5,angle,steps-1) # recursive call

bob.reset()
#squareBob()
#bob.reset()
#triangleBob()

circleBob()
spiral(5, 120, 100)