print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

x=int(input("enter the choice"))
a=int(input("enter the first value"))
b=int(input("enter the second value"))
if(x==1):
    c=a+b
    print(c)
elif(x==2):
    c=a-b
    print(c)
elif(x==3):
    c=a*b
    print(c)
elif(x==4):
    c=a/b
    print(c)
    
