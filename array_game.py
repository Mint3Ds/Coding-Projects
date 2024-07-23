import random

global counter
counter = 0

First_Line =  ["#","#","#","#","#"]
Second_Line = ["#","#","#","#","#"]
Third_Line =  ["#","#","#","#","#"]
Fourth_Line = ["#","#","#","#","#"]
Fith_Line =   ["#","#","#","#","#"]


Array_grid = [First_Line,Second_Line,Third_Line,Fourth_Line,Fith_Line]

def grid():
    for row in Array_grid:
        for num in row:
            print(num, end=" ")
        print()


def generator():
    global randnum1,randnum2,randnum3,randnum4,randnum5,randnum6
    randnum1 = random.randint(0,4)
    randnum2 = random.randint(0,4)
    randnum3 = random.randint(0,4)
    randnum4 = random.randint(0,4)
    randnum5 = random.randint(0,4)
    randnum6 = random.randint(0,4)
    Array_grid[randnum1][randnum2] = "$"
    Array_grid[randnum3][randnum4] = "$"
    Array_grid[randnum5][randnum6] = "$"
    


# userplace1 = random.randint(0,4)
# userplace2 = random.randint(0,4)
# Array_grid[userplace1][userplace2] = "0"



def movement(userplace1,userplace2,counter):
    userinput = input("""Please enter the following:
          'w' for moving upwards
          'a' for moving to the left
          'd' for moving to the right
          's' for moving downwards
           Answer here:""" )
    
    if userinput == "w":
        if userplace1 - 1 == -1:
            print("you cannot go there as it is out of range.")
        else:
            if userplace1 - 1 == randnum1 and userplace2 == randnum2 or userplace1 - 1 == randnum3 and userplace2 == randnum4 or userplace1 - 1 == randnum5 and userplace2 == randnum6:
                counter = counter + 1
            Array_grid[userplace1 - 1][userplace2] = "0"
            Array_grid[userplace1][userplace2] = "#"
            userplace1 = userplace1 - 1

    elif userinput == "a":
        if userplace2 - 1 == -1:
            print("you cannot go there as it is out of range.")
        else:
            if userplace1 == randnum1 and userplace2 - 1 == randnum2 or userplace1 == randnum3 and userplace2 - 1 == randnum4 or userplace1 == randnum5 and userplace2 - 1 == randnum6:
                counter = counter + 1
            Array_grid[userplace1][userplace2 - 1] = "0"
            Array_grid[userplace1][userplace2] = "#"
            userplace2 = userplace2 - 1
    elif userinput == "d":
        if userplace2 + 1 == 5:
            print("you cannot go there as it is out of range.")
        else:
            if userplace1 == randnum1 and userplace2 + 1 == randnum2 or userplace1 == randnum3 and userplace2 + 1 == randnum4 or userplace1 == randnum5 and userplace2 + 1 == randnum6:
                counter = counter + 1
            Array_grid[userplace1][userplace2 + 1] = "0"
            Array_grid[userplace1][userplace2] = "#"
            userplace2 = userplace2 + 1

    elif userinput == "s":
        if userplace1 + 1 == 5:
            print("you cannot go there as it is out of range.")
        else:
            if userplace1 + 1 == randnum1 and userplace2 == randnum2 or userplace1 + 1 == randnum3 and userplace2 == randnum4 or userplace1 + 1 == randnum5 and userplace2 == randnum6:
                 counter = counter + 1
            Array_grid[userplace1 + 1][userplace2] = "0"
            Array_grid[userplace1][userplace2] = "#"
            userplace1 = userplace1 + 1
    
    print("Your score:", counter)
    
    counter_forscore = 0
    for row in Array_grid:
        for num in row:
            if num == "$":
                counter_forscore = counter_forscore + 1
    if counter_forscore == 0:
        generator()
    # if "$" not in First_Line and Second_Line and Third_Line and Fourth_Line and Fith_Line:
    #     print("i cannt find it")
    #     generator()


    if counter != 10:
        loop(userplace1,userplace2,counter)


def loop(userplace1,userplace2,counter):
    grid()
    movement(userplace1,userplace2,counter)










grid()
generator()
userplace1 = random.randint(0,4)
userplace2 = random.randint(0,4)
Array_grid[userplace1][userplace2] = "0"
print("-------------------------------------------------------------")
grid()
movement(userplace1,userplace2,counter)
grid()
