#Program for calc
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
print("\nx =" + str(x) +"\ny = "+ str(y) )
func=input("Enter calc function : \n Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n")

switcher={
        '1':  "x + y = " +str(x+y),
        '2':  "x - y = " +str(x-y),
        '3':  "x * y = " +str(x*y),
        '4':  "x / y = " +str(x/y),
    }

print(switcher.get(func))
