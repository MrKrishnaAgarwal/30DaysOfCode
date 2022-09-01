#String Manipulation

word = "Krishna"
word1= input("Enter first word: ")
word2= input("Enter second word: ")
print("The word is:",word)

def count_words(word):
    return len(word)
print(word, "has", count_words(word) , "digits")

def string_reverse(word):
    return word[::-1]
print(word, "reversed is", string_reverse(word))

def string_concat(word1, word2):
    return word1 + word2
print(word1, "concatenated with", word2, "is", string_concat(word1, word2))