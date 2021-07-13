#printing pattern
n=int(input("enter a number:"))  #user input
for i in range(n+1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()