import random
import time
from lists import yes_words 
from lists import cards 
from lists import dealer_quotes 
from lists import fold_typos
from lists import call_typos
from lists import raise_typos
from lists import check_typos


#variables
starting_chips = 100
playerstack = starting_chips
robotstack = starting_chips
player_card1 = []
player_card2 = []
remaining_cards = 52
card_confidence = 0
pot = 0

def play (play_input):
    player_chips = playerstack
    robot_chips = robotstack

    if play_input in yes_words:
        result = chip_checker(player_chips, robot_chips)
        if result == "true":
            print("\n\n\nshuffling cards...\n\n\n")
            time.sleep(0.8)
            random.shuffle(cards)
            #Dealer quotes
            if random.randint(0,10) < 5:
               print(f"\n\n'{random.choice(dealer_quotes)}...'\n\n")
               time.sleep(0.8)
            else:
               print("...\n\n")
            deal_player_cards()
            deal_robot_cards()
            print(f"\nchips: {playerstack}")
            check_or_bet_preflop(input("5 chips to play: call, raise, or fold: "))


    else:
        print("have fun doing whatever else")


def chip_checker(player_chips, robot_chips):
    player_chips = playerstack
    robot_chips = robotstack
    
    if player_chips >= 1:
     if robot_chips >= 1:
      return "true" 
     else:
      print("dang you beat the robot!")
      return "false"
    else:
      if robot_chips >= 1:
        print("you suck")
        return "false"
      else:
        print("how did you guys both lose your chips???")
        return "false"

def cards_left():
   global remaining_cards
   remaining_cards -= 1
   return remaining_cards

def deal_player_cards():
   player_card1 = cards[cards_left()]
   player_card2 = cards[cards_left()]
   print(f"your hand is...", end="")
   time.sleep(2)
   print(f" \n\n\n {player_card1}, ", end="")
   time.sleep(2)
   print(f"{player_card2}\n")
   time.sleep(2)

def deal_robot_cards():
   robot_card1 = cards[cards_left()]
   robot_card2 = cards[cards_left()]
   #print(f"robot hand is \n\n\n {robot_card1}, {robot_card2}\n\n")

def check_or_bet_preflop(decision):
    if decision in fold_typos:
        print("you fold!")
        print("revealed rest of deck")
        print(cards)
        play(input(" do you want to play again?: "))
    elif decision in raise_typos:
       player_raise_amount(input("please enter the amount you want to raise by: "))
    elif decision in call_typos:
       print("you'd call but i havent gotten there yet")
    else:
       check_or_bet_preflop(input("please type: fold call or raise: "))

def robot_mind(decision, amount):
   if decision == "subtract":
     card_confidence += amount
   
   pass

def player_raise_amount(amount):
   global pot
   global playerstack
   if amount.isdigit():
      amount = int(amount)
      if amount > playerstack:
         print("you dont have that much")
         player_raise_amount(input("please enter a valid amount: "))
      else:
         if amount >= 5:
            pot += amount
            playerstack -= amount
            print(f"pot is now {pot}")
            print(f"your stack is now {playerstack}")
         elif amount <= 5:
            print("minimum raise is 5 chips")
            player_raise_amount(input("please enter a valid raise amount: "))
         else:
            print("please put a number")
            player_raise_amount(input("please enter a valid raise amount: "))
   else:
      player_raise_amount(input("numbers only please: "))


print("\n\n\nWelcome to the Poker Game!\n\n\nThis is No Limit Texas Hold'em")
play(input(" do you want to play: "))


