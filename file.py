list1=["first line\n","second line\n","third line\n","fourth line\n"]
f=open("test.txt","w")
f.writelines(list1)
f.close()
f=open("test.txt","r")
lines=f.readlines()
print("readline():",lines)
f.close()
