import random

options = ["rock", "paper", "scissors"]

def get_choices():
#variables
    player_choice = input("Enter a choice (rock, paper, scissors):")
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}
    return choices

#print(choices)
#Functions only run in a code if it is called
#dictionary "key" : "value"

#player : player_choice
#computer : computer_choice

def check_win(player, computer):  
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
      return "It's a tie"
  elif player == "rock": 
      return "Rock smashes scissors! You win!" if computer == "scissors" else "Paper covers rock! You lose."
  elif player == "paper": 
      return "Paper covers rock! You win!" if computer == "rock" else "Scissors cuts paper! You lose."
  elif player == "scissors": 
      return "Scissors cuts paper! You win!" if computer == "paper" else "Rock smashes scissors! You lose."
  else:
      return "Rock smashes scissors You lose."
    

#Calling the check win function  

choices = get_choices()

result = check_win(choices ["player"], choices ["computer"])
print(result)


