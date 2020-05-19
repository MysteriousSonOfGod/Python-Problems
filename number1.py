#import Math

number = float(input("Enter a number>>  "))

if number == 0:
    print("zero")
    
elif number < 0:
    print("Number is negative")
    if abs(number) < 1:
        print("Small is small it is < 1")
    
elif number > 0:
    print("Number is Positive ")
    if abs(number) > 1000000:
        print("Number is Large it is > 1000000 ")

else:
    print()


#End