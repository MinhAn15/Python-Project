def read_todos(file_path):
    with open(file_path, 'r', encoding= 'utf-8') as file_read:
        todos =  file_read.readlines()
    return todos
def write_todos(file_path):
    with open(file_path, 'w', encoding= 'utf-8') as file_write:
        file_write.writelines(todos)
    return
file_path = input("Enter a file path: ")
while True:
    action = input("Type \"add\", \"show\", \"edit\" or \"complete \": ").strip().lower()
    match action:
        case "add":
            todos = read_todos(file_path)
            
            todo = input("Enter a todo: ").strip() + "\n"
            todos.append(todo)
            
            write_todos(file_path)
            
        case "show":
            todos = read_todos(file_path)
            
            for ind, val in enumerate(todos):
                row = f"{ind + 1} ▶\t{val}"
                print(row, end='')
        case "edit":
            todos = read_todos(file_path)
            
            existing_todo_index = int(input("Enter a number: ")) - 1
            new_todo = input("Enter new todo: ")
            todos[existing_todo_index] = new_todo + '\n'
            
            write_todos(file_path)
        case "complete":
            todos = read_todos(file_path)
            
            ind_remove = int(input("Enter a number of todo completed: ")) - 1
            todo_to_remove = todos[ind_remove].strip('\n')
            todos.pop(ind_remove)
            
            write_todos(file_path)
            print(f"Todo \"{todo_to_remove}\" has removed from the list.")
        case "quit":
            break
    
    