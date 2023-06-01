from turtle import *

screen = Screen()
screen.setup(height=720, width=1280)
shape('turtle')

speed(5)
def run():
    height = int(input("Input the height of the pyramid: "))
    if height < 1:
        height = 1
    elif height > 8:
        height = 8
    else:
        height = height
    
    def second():
        penup()
        goto(50,50)
        pendown()
        for i in range(height - 1):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
    
    def third():
        penup()
        goto(100,100)
        pendown()
        for i in range(height - 2):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
    def fourth():
        penup()
        goto(150,150)
        pendown()
        for i in range(height - 3):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
    def fifth():
       penup()
       goto(200,200)
       pendown()
       for i in range(height - 4):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)     
    def sixth():
        penup()
        goto(250,250)
        pendown()
        for i in range(height - 5):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50) 
    def seventh():
        penup()
        goto(300,300)
        pendown()
        for i in range(height - 6):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
    def eighth():
        penup()
        goto(350,350)
        pendown()
        for i in range(height - 7):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
    """def ninth():
        penup()
        goto(400,400)
        pendown()
        for i in range(height - 8):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
    def tenth():
        penup()
        goto(450,450)
        pendown()
        for i in range(height - 9):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)    """             

    for i in range(height):
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)

    
    if height == 2:
        second()

    elif height == 3:
        second()
        third()
          
    
    elif height == 4:
        second()
        third()
        fourth()
        
    
    elif height == 5:
        second()
        third()
        fourth()
        fifth()
        

    elif height == 6:
        second()
        third()
        fourth()
        fifth()
        sixth()
        

    elif height == 7:
        second()
        third()
        fourth()
        fifth()
        sixth()
        seventh()
        
    elif height == 8:
        second()
        third()
        fourth()
        fifth()
        sixth()
        seventh()
        eighth()
        
    """elif height == 9:
        second()
        third()
        fourth()
        fifth()
        sixth()
        seventh()
        eighth()
        ninth()
        
    elif height == 10:
        second()
        third()
        fourth()
        fifth()
        sixth()
        seventh()
        eighth()
        ninth()
        tenth()"""

        


        
        

run()
done()