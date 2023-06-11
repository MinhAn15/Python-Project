user_prompt = "Type \"add\", \"show\", \"edit\" or \"quit\": "

todos = []

while True:
    action = input(user_prompt).strip().lower()
    match action:
        case "add":
            with open('data.txt', 'r', encoding= 'utf-8') as file_read:
                todos =  file_read.readlines()
           
            
            todo = input("Enter a todo: ").strip() + "\n"
            todos.append(todo)
            
            with open('data.txt', 'w', encoding= 'utf-8') as file_write:
                file_write.writelines(todos)
            
        case "show":
            with open('data.txt', 'r', encoding= 'utf-8') as file_read:
                todos =  file_read.readlines()
            
            for ind, val in enumerate(todos):
                row = f"str(int({ind}) + 1) ▶\t{val}"
                print(row, end='')
        case "edit":
            with open('data.txt', 'r', encoding= 'utf-8') as file_read:
                todos =  file_read.readlines()
            
            existing_todo_index = int(input("Enter a number: ")) - 1
            new_todo = input("Enter new todo: ")
            todos[existing_todo_index] = new_todo
        case "complete":
            with open('data.txt', 'r', encoding= 'utf-8') as file_read:
                todos =  file_read.readlines()
            
            num = int(input("Enter a number of todo completed: ")) - 1
            todos.pop(num)
        case "quit":
            break
    
    