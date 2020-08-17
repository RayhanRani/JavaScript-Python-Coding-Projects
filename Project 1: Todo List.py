todo = []
while True:
  choice=input("What would you like to do with your to do list? \n 1. Add a task \n 2. Remove a task \n 3. Exit \n Type in the number here: ")
  print("")
  if choice=="1":
    task=input("Please type in the task you would like to add: ")
    todo.append(task)
    print("Here is your updated list")
    print(todo)
    print()
  elif choice=="2":
    task2=input("Please type in the task number you would like to remove: ")
    print()
    if int(task2)>len(todo):
      task2=input("PLease type in a more reasonable number of the task you would like to remove: ")
      todo.remove(todo[int(task2)-1])
      print("Here is your updated list")
      print(todo)
      print()
    else:
      todo.remove(todo[int(task2)-1])
      print("Here is your updated list")
      print(todo)
      print()
  else:
    print("Here is your updated list")
    print(todo)
    print()
    break
    
    
