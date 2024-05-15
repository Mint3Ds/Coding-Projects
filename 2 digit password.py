from turtle import *
import random


screen = Screen()
screen.setup(width=750, height=750)

a = Turtle()
a.shape('turtle')
a.speed(9)
b = Turtle()
b.shape('turtle')
b.speed(9)


def one():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    x = 250
    a.penup()
    a.goto(-200,250)
    a.pendown()
    a.right(90)
    a.forward(x)
    a.left(90)
    a.forward(50)
    a.right(180)
    a.forward(100)
    a.penup()
    a.goto(-200,250)
    a.pendown()
    a.left(45)
    a.forward(60)

def two():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 130
    a.penup()
    a.goto(-280,250)
    a.pendown()
    a.left(0)
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)

def three():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.penup()
    a.goto(-280,250)
    a.pendown()
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.backward(x)
    a.left(90)
    a.forward(x)
    a.right(90)
    a.forward(x)
    

def four():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.penup()
    a.goto(-190,200)
    a.pendown()
    a.right(135)
    a.forward(x)
    a.left(135)
    a.forward(100)
    a.left(90)
    a.forward(x-20)
    a.right(180)
    a.forward(2*(x-20))

def five():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.penup()
    a.goto(-150,250)
    a.pendown()
    a.right(180)
    a.forward(120)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.right(90)
    a.forward(x)


def six():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.goto(-150,220)
    a.pendown()
    a.right(180)
    a.forward(x)
    a.left(90)
    a.forward(2*x)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)

def seven():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.goto(-250,200)
    a.pendown()
    a.forward(x)
    a.right(90+20)
    a.forward(x+70)

def eight():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.goto(-260,250)
    a.pendown()
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.right(90)
    a.forward(x)
    a.right(180)
    a.forward(x*2)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)

def nine():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.goto(-150,250)
    a.pendown()
    a.right(180)
    a.forward(x)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)
    a.left(90)
    a.forward(x)
    a.right(180)
    a.forward(x *2)

def zero():
    a.penup()
    a.goto(-350,-100)
    a.pendown()
    for l in range(2):
        a.forward(300)
        a.left(90)
        a.forward(400)
        a.left(90)
    a.penup()
    x = 120
    a.goto(-260,250)
    a.pendown()
    a.forward(x)
    a.right(90)
    a.forward(x * 2)
    a.right(90)
    a.forward(x)
    a.right(90)
    a.forward(x * 2)



def oneB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    x = 250
    b.penup()
    b.goto(200,250)
    b.pendown()
    b.right(90)
    b.forward(x)
    b.left(90)
    b.forward(50)
    b.right(180)
    b.forward(100)
    b.penup()
    b.goto(200,250)
    b.pendown()
    b.left(45)
    b.forward(60)

def twoB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 130
    b.penup()
    b.goto(130,250)
    b.pendown()
    b.left(0)
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)

def threeB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.penup()
    b.goto(150,250)
    b.pendown()
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.backward(x)
    b.left(90)
    b.forward(x)
    b.right(90)
    b.forward(x)


def fourB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.penup()
    b.goto(210,200)
    b.pendown()
    b.right(135)
    b.forward(x)
    b.left(135)
    b.forward(100)
    b.left(90)
    b.forward(x-20)
    b.right(180)
    b.forward(2*(x-20))

def fiveB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.penup()
    b.goto(250,250)
    b.pendown()
    b.right(180)
    b.forward(120)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.right(90)
    b.forward(x)


def sixB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.goto(250,220)
    b.pendown()
    b.right(180)
    b.forward(x)
    b.left(90)
    b.forward(2*x)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)

def sevenB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.goto(150,200)
    b.pendown()
    b.forward(x)
    b.right(90+20)
    b.forward(x+70)

def eightB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.goto(150,250)
    b.pendown()
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.right(90)
    b.forward(x)
    b.right(180)
    b.forward(x*2)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)

def nineB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.goto(250,250)
    b.pendown()
    b.right(180)
    b.forward(x)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)
    b.left(90)
    b.forward(x)
    b.right(180)
    b.forward(x *2)

def zeroB():
    b.penup()
    b.goto(50,-100)
    b.pendown()
    for l in range(2):
        b.forward(300)
        b.left(90)
        b.forward(400)
        b.left(90)
    b.penup()
    x = 120
    b.goto(150,250)
    b.pendown()
    b.forward(x)
    b.right(90)
    b.forward(x * 2)
    b.right(90)
    b.forward(x)
    b.right(90)
    b.forward(x * 2)


def mainfunction():
        global storageA 
        global storageB
        while True:
            counter = 1
            if counter == 1:
                storageA = counter
                one()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 2:
                storageA = counter
                two()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 3:
                storageA = 3
                three()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 4:
                storageA = 4
                four()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 5:
                storageA = 5
                five()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 6:
                storageA = 6
                six()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 7:
                storageA = 7
                seven()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 8:
                storageA = 8
                eight()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 9:
                storageA = 9
                nine()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 10:
                storageA = 10
                zero()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    a.clear()
                    a.setheading(0)
                else:
                    break
            if counter == 11:
                counter = 1       
        while True:
            counter = 1
            if counter == 1:
                storageB = counter
                oneB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 2:
                storageB = counter
                twoB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 3:
                storageB = 3
                threeB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 4:
                storageB = 4
                fourB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 5:
                storageB = 5
                fiveB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 6:
                storageB = 6
                sixB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 7:
                storageB = 7
                sevenB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 8:
                storageB = 8
                eightB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 9:
                storageB = 9
                nineB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 10:
                storageB = 10
                zeroB()
                user_input = input("Do you want to increment the number? y/n: ")
                if user_input == "y":
                    counter = counter + 1
                    b.clear()
                    b.setheading(0)
                else:
                    break
            if counter == 11:
                counter = 1       
            

mainfunction()

if storageA == 6 and storageB == 9:
    print("Congratulations! You've saw the puzzle. Good work detective. Now go to this website and download the rest of the files. ")
else:
    print("You're wrong. Hint: Is a funny number")
