# 11. Write a Python function that takes two lists 
# and returns True if they have at least one common member.

list1 = [1,2,3,4,0,2]
list2 = [8,9,0,5,3,10]

list3 = set(list1)
list4 = set(list2)

for x in list3:
    for y in list4:
        if x in list4:
            print(True)
        else:
            print(False)
