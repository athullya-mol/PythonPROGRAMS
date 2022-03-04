def convert(s):
    new=""
    for x in s:
        new +=x
    return new
s=['aswin','vivek','madhav','janu','dhamu','mani']
string=list(convert(s))
print("count of 'a' in the list is")
print(string.count('a'))
