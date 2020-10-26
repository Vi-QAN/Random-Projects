import time
from gameFunctions import *
from account import *
from GuessingGame import *

if __name__ == '__main__':
    entering = True
    chose = True
    current_balance = 0
    acc = Account()
    command_list = [
        '1. Login',
        '2. Create account',
        '3. Top-up',
        '4. Check balance',
        '5. Delete account',
        '6. Exit']
    games_list = [
        '1.Guessing_game']
    rule_explanation = [
        'In this game, ']
    
    print(f"Welcome to the guessing game. \n")
    
    while entering:
        for i in range(len(command_list)):
            print(command_list[i])
        print("\nFrom (1-{len(command_list)}) What are you looking for ?")
        option = int(input_collect2or())
        while option < 1 or option > len(command_list):
            print("Invalid input. Please enter different input: \n")
            option = int(intput_collector())
        option -= 1
        if option == 0:
            print("Please enter your username: \n")
            username = input_collector()
            current_balance = acc[username]
            print(f"Your current balance is {current_balance} $")
            print("Please choose a game: \n")
            for i in range(len(games_list)):
                print(games_list[i])
            option = int(input_collector())
            while ((option < 1) or (option > len(games_list))):
                print("Invalid input. Please enter different input: \n")
                option = int(intput_collector())
            option -= 1
            if option == 0:
                gs = Guessing_game(username,current_balance)
                current_balance = gs.playing(chose)
                acc[username] = current_balance
        elif option ==1:
            print("Please enter your username: \n")
            username = input_collector()
            print("Your account will be allocated 50$")
            acc.create(username, 50)
            current_balance = acc[username]
            print(f"Your current balance is: {current_balance}")
        elif option == 2:
            print("Please enter your username: ")
            username = input_collector()
            current_balance = acc[username]
            print(type(current_balance))
            print("Please enter top-up amount")
            amount = int(input_collector())
            while amount < 0:
                amount = int(input("Invalid input. Please enter different amount: "))
            current_balance = current_balance + amount
            print(f"Topped-up successfully. Your current balance is: {current_balance}")
            acc[username] = current_balance
        elif option == 3:
            print("Please enter your username: ")
            username = input_collector()
            current_balance = acc[username]
            print(f"Your current balance is: {current_balance}")
        elif option == 4:
            print("Please enter your username: ")
            username = input_collector()
            del acc[username]
        elif option == 5:
            print("Exiting")
            entering = False