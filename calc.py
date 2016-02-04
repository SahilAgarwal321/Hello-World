#Program for calc
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
print("\nx =" + str(x) +"\ny = "+ str(y) )
func=int(input("Enter calc function : \n Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n"))

if func==1:
    print("x + y = " +str(x+y))
elif func==2:
    print("x - y = " +str(x-y))
elif func==3:
    print("x * y = " +str(x*y))
elif func==4:
    print("x / y = " +str(x/y))
else:
    print("Enter function choices from 1 to 4")


