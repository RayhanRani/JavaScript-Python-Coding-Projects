import random
import time

print("Welcome to Type Racer. Get ready to type.")
time.sleep(1)
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Type!")
print()
sentences = ["I went to the store to buy groceries", "I went outside to eat dinner", "I play videogames throughout the summer vacation"]
a = random.randint(0,2)
print(sentences[a])
print()
result = input("Type: ")
start = time.time()
end = time.time()
print()
print("You completed the typing in " + str(end-start) + " seconds. Good Job!")
