word=input('enter a word \n')
print('ordinal  values of the word:',word)
for character in word:
    print(character,"=>",ord(character))
