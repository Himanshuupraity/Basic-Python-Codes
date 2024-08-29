x=int(input("Enter the value X"))
y=int(input("Enter the value Y"))
z=int(input("Enter the value Z"))

if(x>y and x>z):
    print("x is largest")
elif(y>z and y>x):
    print("y is largest")
elif(z>x and z>y):
    print("z is largest")
else:
    print("same")
