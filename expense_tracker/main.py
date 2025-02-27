
import json
import os
data_file = "data.json"



def intro():
    print("==================================")
    print("----------Expense_Tracker---------")
    print("==================================")
    print("__________________________________")


def menu_list():
        main_menu = ("add transaction", "see transaction","see balance", "erase transaction", "exit", 
                    "end the program")
        for i, m in enumerate(main_menu, start = 1):
            print(f"{i}. {m}")


def get_user_input():
    while True:
        try:
            user_input = int(input(" Input the number based on the list above: "))
            if user_input in [1,2,3,4,5]:
                return user_input
            else: 
                print("Input not valid, please input the number based on the list")
        except ValueError:
            print("Error pls input the number based on the list: ")


#read and load data from json file

def read_json(filename):
    with open(filename,'r') as file:
        data = json.load(file)
    return data


def load_json(filename):
    if not os.path.exists(data_file):
        with open(data_file, "w") as file:
            json.dump([],file)
    
    with open(filename,'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open (data_file, "w") as file:
        json.dump(data, file, indent=4)

def exit_program(data):
    print('exiting program')
    exit()
  
# Adding Transaction  
        
from datetime import datetime

def add_transaction(data):
    new_id = len(data) + 1
    date = datetime.today(). strftime("%m/%d/%Y")
    category = input("Input the Category: ")
    description = input("Add the Description: ")
    ammount = input("add Ammount, (negative for expense, positive for income): ")
   
    transaction = {   
        "id": new_id,
        "tanggal": date,
        "kategori": category,
        "deskripsi": description,
        "jumlah": ammount
    }
    
    data.append(transaction)
    save_data(data)
    print("Transaction have been added")
    
def see_transaction(data):
    print("\n Transaction list")
    print("-"*40)
    if data < 1:
        print("There is no transaction")
        return
    else: 
        print("Here is your transaction")
        
    for transaction in data:
        print(f"{transaction['id']}. [{transaction['date']}] {transaction['category']} - {transaction['description']}: Rp {transaction['ammount']} ")
        print("-"*40)
    
def delete_transaction(data):
    see_transaction()
    try:
        id_delete = int(input("Input the ID that need to be erase: "))
        data = [t for t in data if t["id"] !=id_delete]
        #deleted_todo = data.pop(id_delete)
        save_data(data)
        print("Your transaction have been erased")
    
    except ValueError:
        print("Input is not valid. Please input the number based on the data: ")
        return(data)
    
def count_balance(data):
    balance = sum(t["ammount"]for t in data )
    print(f"Your balance is : \n Rp{balance} ")


if __name__ == '__main__':
    db = read_json("data_file")
    intro()

def main():
    print("\n Expense Tracker")
    menu_list()
    user_input = get_user_input()
    match user_input:
        case 1:
            add_transaction()
        case 2:
            see_transaction()
        case 3:
            delete_transaction()
        case 4:
            count_balance()
        case 5:
            exit_program()
        case _:
            print("Input is not valid")
            

    
    
    
    
    
    
    
    
    
    
    
    
    