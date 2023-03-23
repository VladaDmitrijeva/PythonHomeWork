text = str(input("Enter the text\n"))
letter = str(input("Enter a letter\n"))

print("Number of letter in the given text is :", + text.count(letter))

text1 = set(text)
for occurrence in text1:
    number = text.count(occurrence)
    print("character '{}' in the text is: {}".format(occurrence, number))