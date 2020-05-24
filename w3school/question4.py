# 4.Write a Python program to get the smallest number from a list.

numbers = [5,9,10,2,9,29,20,100,200,1000,1,22,3]

minimum_number = numbers[0]

for num in numbers:
    if num < minimum_number:
        minimum_number = num
    else:
        minimum_number = minimum_number


#print('Minimum number =',minimum_number)
#Maximum number = 1

def find_minimum(*args):
    minimum = args[0]

    for x in args:
        if x < minimum:
            minimum = x
        else:
            minimum = minimum
    print('Minimum number =',minimum)

#find_minimum(32,3,75,90)
#Minimum number = 3