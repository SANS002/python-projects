import random

def roll():
    #min_value = 1,max_value = 6 for the dice
    roll = random.randint(1,6)
    return roll

while True:
    players =  input("Enter the number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <=4:
            break
        else:
            print("must be 1 to 4 players need " )
    else:
        print("Invalid ,try again")

max_score = 25

players_score = [0 for i in range(players)]# a list for maintaining each player score
            
while max(player_score) < max_score:

    current_score = 0
    
    dice_roll = input("want to roll (y)? : ")
    if dice_roll.lower() == "y":
        value = roll()
    else:
        break

    if value == 1:
        print("You rolled 1 so Turned down ")
        break
    
    else:
        current_score += value
        print('you rolled a',value)

    print("your score is :" current_score)
    
        
        


