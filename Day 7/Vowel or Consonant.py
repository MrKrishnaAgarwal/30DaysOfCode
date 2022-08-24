alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

character = input("Enter a character: ")
if character in vowels:
    print(character + " is a Vowel")
elif character in consonants:
    print(character + " is a Consonant")
else:
    print(character + " is not a Alphabet") 

def show_alphabets():
    print (alphabets)
def show_vowels():
    print (vowels)
def show_consonants():
    print (consonants)
command = input("Use \'a\' to show alphabets, \'v\' show vowels and \'c\' to show consonants: ").lower()

if command == "a":
    show_alphabets()
elif command == "v":
    show_vowels()
elif command == "c":
    show_consonants()
else:
    print("Invalid command")