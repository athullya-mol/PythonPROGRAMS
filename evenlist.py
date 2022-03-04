#Form a list of integers,create a list removing even numbers
n=int(input("Enter a range:"));
list_1=list(range(n));
print(list_1)
for x in list_1:
    if(x%2==0):
       list_1.remove(x)
print("List of removed even integers",list_1);
