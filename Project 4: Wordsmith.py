import random
import time

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()
print("Welcome to Wordamith! In this game, come up with many words as you can only using the 7 letters your are given. Press enter to begin!")
time.sleep(1)
print("Ready... ")
time.sleep(1)
print("Set... ")
time.sleep(1)
print("Go! ")
print("Your random letters are: ")
print()
x = []
for i in range(0,7):
  letters = random.randint(97, 122)
  a = chr(letters)
  x.append(a)
print(x)
print()
score = 0
word = set()
while True:
  phrase=input("Enter a word: ")
  valid=True
  for i in range(len(phrase)):
    if phrase[i] not in x:
      valid=False
  if valid: 
     if phrase in validWords and phrase not in word: 
      score = score + len (phrase)
      print("Word is Valid! Your score is: " + str(score))
print()


