import random

user_wins=0
computer_wins=0
draw=0

options = ["rock","paper","scissors"]

while True:
    
    user_input = input("type rock/paper/scissors or Q to quit: ").lower()
    if user_input=="q":
        break

    if user_input not in options:
        continue

    computer = random.choice(options)
    print("computer:",computer)
    """
    random_number = random.randint(0,2)
    computer = options[random_number]
    print("computer:",computer) above line and this both are same work here
    in this method we randomize
    the options list index numbers
    """
    
    
    if user_input == "rock" and computer =="scissor":
        print("YOU won !")
        user_wins +=1
        
    
    elif user_input == "scissor" and computer =="paper":
        print("YOU won !")
        user_wins +=1
        
    
    elif user_input == "paper" and computer =="rock":
        print("YOU won !")
        user_wins +=1

    elif user_input == computer :
        print("It's a draw ")
        draw +=1
    
    else:
        print("you lost ")
        computer_wins +=1
 
print("your score is :",user_wins)
print("computer score is : ",computer_wins)
print("number of draws are :",draw)
print("Thank you for playing this game ")

        
        
