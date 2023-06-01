def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("1.add|2.minus|3.multiply|4.divide.")
while True:
    test = input("Choose which calculation you would like to do:  ")

    if test in ("1", "2", "3", "4"):
        number1 = input("Put a number: ")
        number1 = int(number1)
        number2 = input("Put another number you would like to calculate with:  ")
        number2 = int(number2)
        
        if test == "1":
            print(number1, "+", number2, "=", add(number1, number2))
        elif test == "2":
            print(number1, "-", number2, "=", minus(number1, number2))
        elif test == "3":
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif test == "4":
            print(number1, "/", number2, "=", divide(number1, number2))
        again = input("Do you wanna calculate more?(yes|no):  ")
        if again == "no":
            print("Bye!, Have a beautiful day")
            break