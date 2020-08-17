a = input("Type in a palindrome word: ")
b=""
def same (a):
  if len(a) == 1:
    print()
    return True
  elif a[0] != a[-1]:
    print()
    return False
  return(same(a[1:-1]))
print(same(a))

