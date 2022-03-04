#create a list of colors from comma separated color names entered by user.Display first and last color
color=(input("enter the colors:"))
n=color.split(",")
print("%s %s"%(n[0],n[-1]))
