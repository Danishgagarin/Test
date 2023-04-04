from cs50 import SQL
from tabulate import tabulate

db = SQL("sqlite:///data.db")

counter_data = 0

def main():
    global counter_data
    #First we give the user Info Relating the Commands that are available
    
    options = "[A]dd, [R]emove, [V]iew, [E]xit"
    if counter_data == 0:
        option_list()
        counter_data += 1
    else:
        print("\033[1m" + options + "\033[0m")
    #Then we Only Accept input , Also error handling

    while True:
        option = input("Choose your option : ")
        if option in ['A','R','V','E']:
            break
        else:
            print("Please enter one of the Above Command")

    #Then here we construct the core mechanism 

    if option == 'A':
        add_details()
        main()
        

    if option == 'R':
        remove_details()
        main()
        

    if option == 'V':
        print_details()
        main()
    
    if option == 'E':
        exit()


def add_details():
    task = input("Type your agenda: ")
    db.execute("INSERT INTO data (agenda) VALUES(?)",(task,))


def remove_details():
    print_details()
    details = db.execute("SELECT * FROM data") 
    print("")
    valid_id = [row['ID'] for row in details]
    while True:
        rm_id = int(input("Which ID do you want to remove? :"))
        if rm_id in valid_id:
            break
        else:
            print("Please enter a valid ID")

    db.execute("DELETE FROM data WHERE ID = ?",(rm_id,))
    reorder()

def print_details():
    detail = db.execute("SELECT * FROM data")
    print(tabulate(detail))

def reorder():
    details = db.execute("SELECT * FROM data ORDER BY ID")
    for i,row in enumerate(details):
        db.execute("UPDATE data SET ID=? WHERE ID=?", i+1, row["ID"])

def exit():
    print("Thank you")

def option_list():
    heading = "WELCOME TO TODO-LIST"
    print("\033[1m" + heading + "\033[0m")
    print("")
    print("'A'- Add new Task")
    print("'R'- Remove a Task")
    print("'V'- View List") 
    print("'E'- EXIT")
    print("")


main()


    
    

