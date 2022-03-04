#find biggest of 3 numbers entered
a=int(input("Enter a first number"));
b=int(input("Enter a second number"));
c=int(input("Enter a third number"));
def max(a,b,c):
    if(a>=b)and(a>=c):
        largest=a;
    elif(b>=a)and(b>=c):
        largest=b;
    else:
        largest=c;
    return largest
print("Biggest Number is",max(a,b,c))
