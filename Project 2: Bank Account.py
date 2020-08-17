account = {"rayhan": "rayhan25"}
money = {"rayhan": 1000}
while True:
  while True:
    username = input("Welcome to the bank! Please log in." + "\nUsername: ")
    password = input("Password: ")
    print()
    if username not in account:
      print ("Please try another username. ")
    elif password != account[username] :
      print("Please try another password. ")
    else:
      break
  while True:
    print("Welcome " + username + ". You currently have " + str(money[username]) + " in your bank account. What would you like to do? ")
    print()
    choice = input(" 1.Make a deposit. \n 2.Make a withdrawal. \n 3.Change your password \n 4.Log out \n Type in the number here: ")
    if choice =="1":
      deposit = input("How much money would you like to deposit? ")
      money[username] = money[username] + int(deposit)
      print()
    elif choice == "2":
      withdraw = input("How much money would you like to withdraw? ")
      money[username] = money[username] - int(withdraw)
      print()
    elif choice == "3":
      change = input("To change your password, please type in your old password: ")
      print()
      if change == account[username]:
        new = input("Please type in yout new password: ")
        account[username] = new
      else:
        print("Your password could not be changed.")
    else:
      print("You have successfully logged out of your bank account.")
      print()
      break
        
     
