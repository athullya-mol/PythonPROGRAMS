#display the given pyramid with step number accepted from user
num=int(input('enter number'))
for row in range(1,num+1):
    for col in range(1,row+1):
        print(row*col,end=" ")
    print()    
