from module.function import read_todos,write_todos
import PySimpleGUI

label = PySimpleGUI.Text("Type in a todo")
input_box = PySimpleGUI.InputText(tooltip="Enter todo ", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=read_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")

window = PySimpleGUI.Window("Andy's Todo App"
                            , layout=[[label], [input_box, add_button], [list_box,edit_button]]
                            , font=('Arial', 25))


while True:
    event, values = window.read()
    if event == 'Add':
        todos = read_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        
        write_todos(todos)
        
    # elif event == "show":
    #     todos = read_todos()
        
    #     for ind, val in enumerate(todos):
    #         row = f"{ind + 1} ▶\t{val}"
    #         print(row, end='')
    elif event == "Edit":
        todo_edit = values['todos'][0]
        new_todo = values['todo']
        
        todos = read_todos()
        existing_todo_index = todos.index(todo_edit)
        
        todos[existing_todo_index] = new_todo 
        
        write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == PySimpleGUI.WIN_CLOSED:
        break

window.close()