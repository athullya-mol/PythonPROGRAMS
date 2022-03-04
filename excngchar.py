#create a string from given string where first and last character exchange
word_1=input("Enter any string: ");
word=list(word_1);
word[0],word[-1]=word[-1],word[0];
word_2="".join([str(elem) for elem in word]);
print("The string after exchange first and last position: ",word_2);
