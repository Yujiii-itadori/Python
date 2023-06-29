import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(['r', 'p', 's']) 

    if user == computer:
        return print('It is a tie')
    
    if win(user, computer):
        return print( 'You won!')

    return print('You lost') 


def win(user, computer):
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
        or (user == 'p' and computer == 'r'):
            return True
        
play()