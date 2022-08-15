import random
import math

def game_rules(user, cpu):
    if (user == 'r' and cpu == 's') or (user == 's' and cpu == 'p') or (user == 'p' and cpu == 'r'):
        return True
    else:
        return False

def play_game():
    user = input("Choose r for rock, p for paper, or s for scissors, any other input will result in a loss for the round! ").lower()
    game_list = ['r', 'p', 's']
    cpu_choice = random.choice(game_list)

    if user not in game_list:
        print("This is not a choice!")
    else:
        if user == cpu_choice:
            return 0
        if game_rules(user, cpu_choice):
            return 1
        else:
            return -1

def best_of_rounds():
    rounds = int(input("How many rounds would you like to play? "))
    user_wins = 0
    cpu_wins = 0
    to_win = math.ceil(rounds/2)
    
    if rounds % 2 != 0:
        while user_wins < to_win and cpu_wins < to_win:
            output = play_game()
            if output == 0:
                print("You have tied with the computer, try again!")
            elif output == 1:
                user_wins += 1
                print("You won!") 
            else:
                cpu_wins += 1
                print("You lost")
        if user_wins > cpu_wins:
            print("You have bested the computer, you have won!")
        else:
            print("You have lost to the Computer's AI! Now they will overthrow us!")
        print("\n")

        print(f"You have won {user_wins} times and the CPU has won {cpu_wins} time out of the series. What a battle!")
    else:
        print("Pick an odd number of rounds so you can properly beat the CPU!")
    

best_of_rounds()