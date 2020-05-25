# 14. Write a Python program to print the numbers of a 
#specified list after removing even numbers from it

list_with_evens    = [3,5,8,2,7,10,11,17,15,13,199,100]

list_without_evens = [3,11,19,17,15,13,197,111,113,115]

new_list = []

for numbers in list_with_evens:
    if numbers % 2 == 0:
        pass
    else:
        new_list.append(numbers)

print(new_list)