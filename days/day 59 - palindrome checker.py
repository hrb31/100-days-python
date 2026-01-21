def is_palindrome(word):
  if len(word) <= 1:
    return True
  else:
    for i in range(len(word)):
      if word[i] != word[len(word) - 1 - i]:
        return False
      else:
        word = word[i+1:len(word) - 1 - i]
        return is_palindrome(word)

print("Palindrome Checker")
print()

word = input("Enter a word: ")
word = word.lower().strip()
print()

if is_palindrome(word):
  print(word, "is a palindrome!")
else:
  print(word, "is not a palindrome!")




