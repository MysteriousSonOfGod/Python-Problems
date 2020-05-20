grade = input("Enter a letter grade A: ")

A = 4
B = 3
C = 2
D = 1
F = 0

if grade == "A+":
    A = A + 0.3
    print("The numeric value is",A)
    
elif grade == "A-":
    A = A - 0.3
    print("The numeric value is",A)
    
elif grade == "A":
    print("The numeric value is",A)
##################    
elif grade == "B+":
    B = B + 0.3
    print("The numeric value is",B)
    
elif grade == "B-":
    B = B - 0.3
    print("The numeric value is",B)
    
elif grade == "B":
    print("The numeric value is",B)
###################    
elif grade == "C+":
    B = B + 0.3
    print("The numeric value is",C)

elif grade == "C-":
    B = B - 0.3
    print("The numeric value is",C)
    
elif grade == "C":
    print("The numeric value is",C)
#################
elif grade == "D":
    print("The numeric value is",D)
    
elif grade == "F":
    print("The numeric value is",F)
