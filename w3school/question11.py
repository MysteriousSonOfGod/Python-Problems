# 11. Write a Python function that takes two lists 
# and returns True if they have at least one common member.



def compare_lists():
    list1 = [1,2,3,4,0,2]
    list2 = [8,9,0,5,3,10]

    for items in list1:
        for items2 in list2:
            if items in list2:
                return True
            else:
                return False

    for list2 in list1:
        print("nakala")



result = compare_lists()
print(result)
