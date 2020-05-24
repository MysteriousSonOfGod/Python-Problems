# 1. Write a Python program to sum all the items in a list

#When a you provide your own set of numbers
def default_numbers():
    list_of_numbers = [1,2,3]
    sum = 0

    for numbers in list_of_numbers:
        sum = sum + numbers

    print('result =',sum)
#default_numbers
#result = 


#Letting the user choose set of numbers
def user_list(*args):
    sum = 0

    for numbers in args:
        sum = sum + numbers

    print('result =',sum)

#user_list(2,3,4,5,6,2)
#result = 22