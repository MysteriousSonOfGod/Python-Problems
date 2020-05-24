# 7. Write a Python program to remove duplicates from a list

#List of duplicates
full_list = [2,12,9,20,20,19,18,92,19,18,18,18,10,2,19,10,2,7,89,72,10,10,2]

list_without_duplicates = []

for numbers in full_list:
    if numbers in list_without_duplicates:
        pass
    else:
        list_without_duplicates.append(numbers)
    
print(list_without_duplicates)
#output >> [2, 12, 9, 20, 19, 18, 92, 10, 7, 89, 72]

