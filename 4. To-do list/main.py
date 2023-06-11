user_prompt = "Type \"add\", \"show\", \"edit\" or \"quit\": "

todos = []

while True:
    action = input(user_prompt).strip().lower()
    match action:
        case "add":
            todo = input("Enter a todo: ").strip().lower()
            todos.append(todo)
        case "show":
            for ind, val in enumerate(todos):
                row = f"{ind} ▶ {val}"
                print(row)
        case "edit":
            existing_todo_index = int(input("Enter a number: ")) - 1
            new_todo = input("Enter new todo: ")
            todos[existing_todo_index] = new_todo
        case "complete":
            num = int(input("Enter a number of todo completed: ")) - 1
            todos.pop(num)
        case "quit":
            break
    
    