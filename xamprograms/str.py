#create a string from given string where first and last characters exchanged
string=input("enter a string")
start=string[0]
end=string[-1]
swapped_string=end+string[1:-1]+start
print(swapped_string)
