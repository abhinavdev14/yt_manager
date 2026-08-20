import json



def load_data():
    try:
        with open('todos.json','r') as file:
            test = json.load(file)
            
            return test
    except FileNotFoundError:
        return []

def save_data(todos):
    with open('todos.json','w') as file:
        json.dump(todos, file)

def add_todo(todos):
    task = input("enter ur task: ")
    status = "pending"
    todos.append({'task': task , 'status': status})
    save_data(todos)

def list_todo(todos):
    for index , todo in enumerate(todos, start=1):
        print(f"{index}.task: {todo['task']}, status: {todo['status']} ")

def mark_todo(todos):
    list_todo(todos)
    index = int(input("konsa mark krna h? : "))
    todos[index - 1]["status"] = "Completed"
    save_data(todos)



def delete_todo(todos):
    list_todo(todos)
    index = int(input("which one ? : "))
    
    if 1<= index <= len(todos):
        del todos[index-1]
        save_data(todos)

    else:
        print("invalid index")

def main():

    while True:

        todos = load_data()

        print("1. Add todo")
        print("2. List Todos")
        print("3. Mark Todo as Completed")
        print("4. Delete Todo")
        print("5. Exit")
        choice = input("enter ur choice: ")

        match choice:
            case '1':
                add_todo(todos)
            case '2':
                list_todo(todos)
            case '3':
                mark_todo(todos)
            case '4':
                delete_todo(todos)
            case '5':
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()



