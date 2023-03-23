# Write a function that takes a string as 
# a parameter and returns the number of vowels (aeiou) in the string. 
# Hint: you can use given_character in "aeiou"

# vowels = ["a","e","i","o","u"]
# count = 0

# word = str(input("Enter the word:\n"))
# for i in range(len(word)):
#     if word[i] in vowels:
#         count += 1
# print("The number of vowels in word is ", count)


def NumberofVowels(word):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            count += 1
            print("The number of vowels in word is ", count)
    return count
            
NumberofVowels("wordword")

    