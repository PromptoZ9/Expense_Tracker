import json
import os

DATA_FILE = "data.json"

# Load data dari JSON file
def load_data():
    if not os.path.exists(DATA_FILE):  # Jika file belum ada, buat file kosong
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Simpan data ke JSON file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def intro():
    print("==================================")
    print("----------Expense_Tracker---------")
    print("==================================")
    

# main_menu
def main_menu():
    menu_list = ("Adding Transaction", "View Transaction", "Erase Transaction", "View Balance", "exit prgram")
    for i, m in enumerate(menu_list, start=1):
        print(f"{i}. {m}")

def exit_program():
    save_data("data.json")
    exit()

# adding transaction
from datetime import datetime
def add_transaction():
    data = load_data()
    new_id = len(data) + 1
    date = datetime.today().strftime('%d/%m/%Y')
    category = input("Input category transaction: ")
    description = input("Transaction description: ") 
    ammount = int(input("ammount of balance (negative for expense, positive for income):  "))
    
    transaction = {   
        "ID" : new_id,
        "Date" : date,
        "Category" : category,
        "Description" : description,
        "Ammount" : ammount
     }
    data.append(transaction)
    save_data(data)
    print("Transaction have been added")
    return data

#View Transaction


#output check
def get_user_input():
    while True:
        try: 
            user_input = int(input("input the number based on the list: "))
            if user_input in [1,2,3,4,5]:
                break
            else : 
                print("input is not valid, please input the number based on the list above: ")
        except ValueError:
            print("input is not valid, please input the number based on the list above: ")


while True:
    intro()
    main_menu()
    user_input = get_user_input()
    match user_input:
        case 1:
            print("Adding Transaction")
            break
        case 2:
            print("Viewing Transaction")
            break
        case 3:
            print("Erasing Transaction")
            break
        case 4:
            print("Counting Balance")
        case 5:
            exit_program()
        case _:
            print("input is not valid")






















