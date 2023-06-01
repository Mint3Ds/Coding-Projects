import random
start= input("""Hello Adventurer! Would you like to play a game of rock, paper scissor?
                You may choose either 'yes' or 'no':       """)

def fusion():
    
    player = input('Pick a choice of "rock", "paper" or "scissor",       ')
    if player == "rock":
        player = 1
    elif player == "scissor":
        player = 2
    elif player == "paper":
        player = 3
    else:
        print("Please type either 'rock', 'paper', 'scissor', as it is.")
        redo = input("Would you like to try again? please pick 'yes' or 'no':")

        if redo == "yes":
            again = input("Pick your choice again:   ")
            if again == "rock":
                player = 1
            elif again == "scissor":
                player = 2
            elif again == "paper":
                player = 3
            else:
                print("You have mistype the words again, please restart the game.")
                    
    
        else:
          print("You have mistype the words again, please restart the game.")



    generator = random.randint(1,3)
    if generator == 1:
        print("I chose rock")
    elif generator == 2:
        print("I chose scissor")
    elif generator == 3:
        print("I chose paper")


    def rematch():
        rematch = input("would you care for a rematch adventurer? Answer with 'yes' or 'no':       ")
        if rematch == "yes":
            fusion()
        else:
            print("Till we meet again adverturer!")


    
    if generator == player:
        print("Is a draw!")
        rematch()
    elif (generator == 1 and player == 3) or (generator ==2 and player == 1) or (generator==3 and player==2):
            print("You sir, are a great player.")
            rematch()
    elif (generator == 1 and player == 2) or (generator ==2 and player == 3) or (generator==3 and player==1):
            print("You fate had been sealed and you've lost.")
            rematch()


if start == 'yes':
    fusion()
else:
    print("Fair Well Adventurer, till we meant again!")



        





    
    


