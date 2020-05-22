#Exercise 36: Vowel or Consonant

vowels = ['A','E','I','O','U']

input_any_letter = input("Input a letter: ")
letter = input_any_letter.upper()

if letter not in vowels:
    if letter == 'Y':
        print("Sometimes Y is a vowel, and sometimes Y is a consonant")
    else:
        print("The letter",input_any_letter.upper(),"is a consonant.")

elif letter in vowels:
    print("The letter",input_any_letter.upper(),"is a vowel.")

else:
    print('Invalid input.....')