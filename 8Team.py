word = input("Enter a word: ").lower()
char = input("Enter a character: ").lower()
char = char[0]
for letter in range(len(word)):
    if word[letter] == char:
        print(char.upper(), end="")
    else: print(word[letter], end="")