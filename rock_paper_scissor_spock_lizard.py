# Rock-paper-scissors-lizard-Spock game.


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random
import math

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        return "error"
    

    
    
    

def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
        return "error"
    
    
   
    

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print '\n'
    
    

    # print out the message for the player's choice
    print "player chooses ",player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "computer chooses ",comp_choice

    # compute difference of comp_number and player_number modulo five
    a=(comp_number-player_number)%5
    if a==1 or a==2:
        print "computer wins"
    elif a==3 or a==4:
        print "player wins" 
    
   

    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




