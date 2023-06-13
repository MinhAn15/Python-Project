from module.function import read_todos, write_todos
import time


now = time.strftime('%Y-%m-%d %H:%M:%S')
print(f"It is at {now}")
file_path = input("Enter a file path: ")
while True:
    action = input("Type \"add\", \"show\", \"edit\" or \"complete \": ").strip().lower()
    
    if action == "add":
        todos = read_todos(file_path)
        
        todo = input("Enter a todo: ").strip() + "\n"
        todos.append(todo)
        
        write_todos(file_path, todos)
        
    elif action == "show":
        todos = read_todos(file_path)
        
        for ind, val in enumerate(todos):
            row = f"{ind + 1} ▶\t{val}"
            print(row, end='')
    elif action == "edit":
        todos = read_todos(file_path)
        
        existing_todo_index = int(input("Enter a number: ")) - 1
        new_todo = input("Enter new todo: ")
        todos[existing_todo_index] = new_todo + '\n'
        
        write_todos(file_path, todos)
    elif action == "complete":
        todos = read_todos(file_path)
        
        ind_remove = int(input("Enter a number of todo completed: ")) - 1
        todo_to_remove = todos[ind_remove].strip('\n')
        todos.pop(ind_remove)
        
        write_todos(file_path, todos)
        print(f"Todo \"{todo_to_remove}\" has removed from the list.")
    elif action == "quit":
        break
    
    