import time
import random

print("Welcome to Blackjack!")
print()
time.sleep(1)
print("Get ready to play.")
print()
cont = True
while True: 
  numbers = random.randint(2,11)
  numbers2 = random.randint(2,11)
  numbers3 = random.randint(2,11)
  player = []
  print("Here is your hand: ")
  player.append(numbers)
  player.append(numbers2)
  print(player)
  cont = True
  if sum(player) == 21:
    print("You have met exactly 21. :)")
  if cont == True:
    hors = "H"
    while hors == "H":
      hors = input("Type in H to hit or S to stay: ")
      while True:
        if hors == "H" or hors == "S":
          break
        else:
          print("This was an invalid letter. Please try again by entering a valid action.")
      if hors == "H":
        player.append(numbers3)
        print(player)
        if sum(player) > 21:
          print("You busted. :(")
          cont = False
        elif sum(player) == 21:
          print("You have met exactly 21. :)")
    print(player)
    print()
    
  if cont == True:      
    num = random.randint(2,11)
    num2 = random.randint(2,11)
    num3 = random.randint(2,11)
    dealer = []
    print("Here is the dealer's hand: ")
    dealer.append(num)
    dealer.append(num2)
    print(dealer)
    if sum(dealer) == 21:
      print("You have met exactly 21. :)")
      while sum(dealer) <= 17:
        dealer.append(num3)
        if sum(dealer) == 21:
          print("You have met exactly 21. :)")
        elif sum(dealer) > 21:
          print("You busted. :(")
          cont = False
        else:
          break
    print(dealer)
  
    print("Here is the player's total number: " + str(sum(player)))
    print("Here is the dealer's total number: " + str(sum(dealer)))
    print()
    if sum(player) > sum(dealer):
      print("Congrats! The player has won.")
    else:
      print("Congrats! The dealer has won.")
      if sum(player) and sum(dealer) == 21:
        print("Congrats! You both are winners!")
      elif sum(player) == sum(dealer):
        print("On no! You both have tied. Please play again")
    print()


