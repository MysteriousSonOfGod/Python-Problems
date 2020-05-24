# 3. Write a Python program to get the largest number from a list

numbers = [5,9,10,2,9,29,20,100,200,1000,1,22,3]

maximum_number = numbers[0]

for num in numbers:
    if num > maximum_number:
        maximum_number = num
    else:
        maximum_number = maximum_number


#print('Maximum number =',maximum)
#Maximum number = 1000

def find_maximum(*args):
    maximum = args[0]

    for x in args:
        if x > maximum:
            maximum = x
        else:
            maximum = maximum
    print('Maximum number =',maximum)

#find_maximum(32,3,75,90)
#Maximum number = 90