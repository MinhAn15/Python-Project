user_prompt = "Type \"add\", \"show\", \"edit\" or \"quit\": "

todos = []

while True:
    action = input(user_prompt).strip().lower()
    match action:
        case "add":
            file_read = open('data.txt', 'r', encoding='utf-8')
            todos =  file_read.readlines()
            file_read.close()
            
            todo = input("Enter a todo: ").strip() + "\n"
            todos.append(todo)
            
            file_write = open('data.txt', 'w', encoding='utf-8')
            file_write.writelines(todos)
            file_write.close()
        case "show":
            file_read = open('data.txt', 'r', encoding='utf-8')
            todos =  file_read.readlines()
            file_read.close()
            
            for ind, val in enumerate(todos):
                row = f"{ind} ▶\t{val}"
                print(row, end='')
        case "edit":
            file_read = open('data.txt', 'r', encoding='utf-8')
            todos =  file_read.readlines()
            file_read.close()
            
            existing_todo_index = int(input("Enter a number: ")) - 1
            new_todo = input("Enter new todo: ")
            todos[existing_todo_index] = new_todo
        case "complete":
            file_read = open('data.txt', 'r', encoding='utf-8')
            todos =  file_read.readlines()
            file_read.close()
            
            num = int(input("Enter a number of todo completed: ")) - 1
            todos.pop(num)
        case "quit":
            break
    
    