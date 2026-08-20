import json



def load_data():
    try:
        with open('todos.txt','r') as file:
            test = json.load(file)
            print(test)
            return test
    except FileNotFoundError:
        return []

def save_data(todos):
    with open('todos.txt','w') as file:
        json.dump(todos, file)
def add_todo():
    pass
def list_todo():
    pass
def mark_todo():
    pass
def delete_todo():
    pass

def main():

    while True:

        func = load_data()

        print("1. Add todo")
        print("2. List Todos")
        print("3. Mark Todo as Completed")
        print("4. Delete Todo")
        print("5. Exit")
        choice = input("enter ur choice: ")

        match choice:
            case '1':
                add_todo()
            case '2':
                list_todo()
            case '3':
                mark_todo()
            case '4':
                delete_todo()
            case '5':
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()



