# -*- coding: utf-8 -*-
import random
from gameFunctions import *
class Guessing_game:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance - 10
        
    def playing(self,want_to_play):
        is_InCorrect = True
        print("Entering Guessing Game")
        while want_to_play:
            rand = random.randint(1,20)
            print("A random number was generated. \nPlease guess the number:")
            guess = input_collector()
            guess = guess_checker(guess, is_InCorrect)
            attempts = self.announce(rand, guess, is_InCorrect)
            self.prize_award(attempts)
            print("Do you want to play again. Press Y if you want and N if you do not")
            choice = input_collector()
            choice = choice_checker(choice, is_InCorrect)
            if choice == "Y":
                print("Renewing the game ")
            else:
                print(f"Your current balance: {self.balance} \nExisting")
                want_to_play = False
        return self.balance
            
    def announce(self, rand, guess,is_InCorrect ):
        attempts = 1
        while (rand != guess):
            if (guess < rand):
                print("Your guess is lower than generated number \n Try again")
                guess = input_collector()
                guess = guess_checker(guess, is_InCorrect)
            elif (guess > rand):
                print("Your guess is higher than generated number \n Try again")
                guess = input_collector()
                guess = guess_checker(guess, is_InCorrect)
            attempts +=1
        return attempts

    def prize_award(self,attempts):
        prizes = [50,40,30,20,10]
        rank = [
             "Congratulation !!! You won 1st prize 50$",
             "Congratulation !!! You won 2nd prize 40$",
             "Congratulation !!! You won 3rd prize 30$",
             "Congratulation !!! You won 4th prize 20$",
             "Congratulation !!! You won 5th prize 10$"
                ]
        if (attempts <= 5):    
            print(f"{rank[attempts-1]} after {attempts} attempts. ")
            self.balance += prizes[attempts-1]
        else:
            print ("Unlucky !!!")