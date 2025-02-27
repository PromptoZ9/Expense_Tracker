import json

def read_json(filename):
    with open(filename, 'r') as file: 
        data = json.load(file)
    return data

def save_data(filename, dt):
    with open(filename, "w") as f:
        json.dump(dt, f)


def login(dt):
    username = input('username: ')
    password = input('password: ')
    if username in dt and dt[username]['password'] == password:
        print(f'login success!, welcome {username}')
        return dt[username]
    else: 
        raise ValueError('login failed, username/password is incorrect')

def register(dt):
    username = input('username: ')
    password1 = input('password: ')
    password2 = input('confirm password: ')
    if password1 == password2 and username not in dt:
        dt[username] = {"name": username, "password": password1, 'transaction': [] }
        save_data("dt.json", dt)
        exit("Register success")
    else:
        raise Exception('username/password did not match, or username already been used')


def intro():
    print("==================================")
    print("----------Expense_Tracker---------")
    print("==================================")
    

# main_menu
def main_menu():
    menu_list = ("Adding Transaction", "View Transaction","Edit transaction list","Erase Transaction", "View Balance", "exit prgram")
    for i, m in enumerate(menu_list, start=1):
        print(f"{i}. {m}")

# adding transaction
from datetime import datetime
def add_transaction(transaction):
    
    date = datetime.today().strftime('%d/%m/%Y')
    category = input("Input category transaction: ")
    description = input("Transaction description: ") 
    ammount = int(input("ammount of balance (negative for expense, positive for income):  "))
    
    transaction = {   
        "Date" : date,
        "Category" : category,
        "Description" : description,
        "Amount" : ammount
     }
    transaction.append(transaction)
    print("Transaction have been added")
    return transaction

def view_transaction(transaction):
    for i, transaction in enumerate (transaction, start = 1):
        print(f"{i}. {transaction['Date']} {transaction['Category']} - {transaction['Description']}: Rp{transaction['Amount']}")
    print("="*50)
    if not transaction:
        print("There is no Transaction")
        return transaction

    


def erase_transaction(transaction):
    while True:
        transaction_del = int(input('Input the transaction number that need to be erased, type 0 to cancel: ')) - 1
        if transaction_del == -1:
            return
        elif transaction_del >= 0 and transaction_del < len(transaction):
            deleted_t = transaction.pop(transaction_del)
            print(f"your transaction on {deleted_t['Description']} has been deleted")
        else:
            print("The number isn't match, please input the number based on the list")

def counting_balance(transaction):
    balance = sum(t['Amount'] for t in transaction)
    print(f"Your balance is: Rp{balance}")


def exit_program(dt):
    save_data("dt.json", dt)
    exit()


def get_user_input():
    while True:
        try: 
            user_input = int(input("input the number based on the list: "))
            if user_input in [1,2,3,4,5,6]:
                return user_input
            else : 
                print("input is not valid, please input the number based on the list above: ")
        except ValueError:
            print("input is not valid, please input the number based on the list above: ")

if __name__ == '__main__':
    dt = read_json('dt.json')
    intro()
    
    login_or_register = input('login or register: ')
    match login_or_register:
        case 'login':
            user = login(dt)
        case 'register':
            register(dt)
        case _:
            raise ValueError('Invalid input, please input login or register')    

    
while True:
    main_menu()
    user_input = get_user_input()
    match user_input:
        case 1:
            print("Adding Transaction")
            add_transaction(user['transaction'])
        case 2:
            print("Here is the list of your transaction so far: ")
            view_transaction(user['transaction'])
            
        case 3:
            print("Edit your transaction list")
            view_transaction(user['transaction'])
            tr_input = int (input("choose the transaction number that needs to be edited: ")) - 1
            if tr_input < 0:
                raise ValueError('Input is not on the list, please input the number base on the list: ')
            print(user['transaction'][tr_input])
            for i, key in enumerate(user['transaction'][tr_input], start=1):
                print(f"{i}. {key}")
            user_input = int(input("choose the number on the list to edit your transaction: "))
            match user_input: 
                case 1:
                #Date
                    new_date = user['transaction'][tr_input]['Date'] = input('Enter the new (DD/MM/YYYY): ')
                    formatted_date = datetime.strptime(new_date, "%d/%m/%Y")
                    print("The current transaction has been updated!")
                case 2:
                #Category
                    user['transaction'][tr_input]['Category'] = input('Enter the new category for this transaction: ')
                    print("The current transaction has been updated!")
                case 3:
                #Description
                    user['transaction'][tr_input]['Description'] = input('Enter the new description for this new transaction: ')
                    print("The current transaction has been updated!")
                case 4:
                #Amount 
                    user['transaction'][tr_input]['Amount'] = int(input('Enter the new description for this new transaction: '))
                    print("The current transaction has been updated!")
        case 4:
            view_transaction(user['transaction'])
            erase_transaction(user['transaction'])
            print("Returning to main menu")
        case 5:
            view_transaction(user['transaction'])
            print("Counting Balance")
            counting_balance(user['transaction'])
            print("Returning to main menu")
        case 6:
            print("exiting program")
            exit_program(dt)
        case _:
            print("Input is not valid")
        





















































