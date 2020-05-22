#Exercise 35: Dog Years

human_years = int(input("Enter human year: "))
dog_years = 0

if human_years <= 2:
    dog_years = human_years * 5.225
    print(human_years,'human years =',dog_years,'dog years')


#For this part iinitialised "initial" to subtract 2 from the human years
#And after multiplying the remainder with 4 then i can add 10.50 as the 
#The first two years
elif human_years > 2:
    initial   = human_years - 2
    dog_years = (initial * 4) + 10.5
    print(human_years,'human years =',dog_years,'dog years')

elif human_years < 1:
    print("Error!")

else:
    print("Invalid input.....")    