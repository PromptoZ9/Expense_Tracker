#import json

print("==================================")
print("----------Expense_Tracker---------")
print("==================================")
print("\n")

# adding transaction
from datetime import datetime

date = datetime.today().strftime('%d/%m/%Y')
category = input("Input category transaction: ")
description = input("Transaction description: ") 
ammount = int(input("ammount of balance (negative for expense, positive for income):  "))
                        

# main_menu

print("\n Expense Tracker")
print("\n")
print("1. Adding Transaction")
print("2. View Transaction")
print("3. Erase Transaction")
print("4. View Balance")
print("5. exit prgram")
print("\n")

#user_input

while True:
    try: 
        user_input = int(input ("input the number based on the list: "))
        if user_input in [1,2,3,4,5]:
            break
        else : 
            print("input is not valid, please input the number based on the list above: ")
    except ValueError:
        print("input is not valid, please input the number based on the list above: ")

if  user_input == 1:
    print("Adding Transaction")
elif user_input == 2:
    print("Viewing Transaction")
elif user_input == 3:
    print("Erasing Transaction")
elif user_input == 4:
    print("Counting Balance")
elif user_input == 5:
    print("exit program")

    





