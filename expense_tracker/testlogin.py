import json

def read_json(filename):
    with open(filename, 'r') as file: 
        data = json.load(file)
    return data

def save_data(filename, dt):
    with open(filename, "w") as f:
        json.dump(dt, f, indent=4)

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

def main_menu():
    menu_list = ("Adding Transaction", "View Transaction", "Erase Transaction", "View Balance", "exit prgram")
    for i, m in enumerate(menu_list, start=1):
        print(f"{i}. {m}")


from datetime import datetime
def add_transaction():
    data = read_json()
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



if __name__ == "__main__": 
    dt = read_json('dt.json')
    add_transaction()