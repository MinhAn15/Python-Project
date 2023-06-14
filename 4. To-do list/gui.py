from module.function import read_todos,write_todos
import PySimpleGUI
import time

PySimpleGUI.theme("DarkGreenYellow155")

clock = PySimpleGUI.Text('', key='clock')
label = PySimpleGUI.Text("Type in a todo")
input_box = PySimpleGUI.InputText(tooltip="Enter todo ", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=read_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")
window = PySimpleGUI.Window("Andy's Todo App"
                            , layout=[[clock],[label], [input_box, add_button], [list_box,edit_button], [complete_button,exit_button]]
                            , font=('Arial', 25))


while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime('%b %d %Y %H:%M%S'))
    print(event)
    print(values)
    if event == 'Add':
        todos = read_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        try:
            todo_edit = values['todos'][0]
            new_todo = values['todo']
            
            todos = read_todos()
            existing_todo_index = todos.index(todo_edit)
            
            todos[existing_todo_index] = new_todo 
            
            write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            PySimpleGUI.popup("Select Item first!", font=("Helvetica", 20))
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == "Complete":
        try:    
            todo_complete = values['todos'][0]
            todos = read_todos()
            todos.remove(todo_complete)
            
            write_todos(todos)        
            window['todos'].update(values=todos)
            
            window['todo'].update(value='')
        except IndexError:
            PySimpleGUI.popup("Select Item first!", font=("Helvetica", 20))
    elif event == "Exit":
        break
    elif event == PySimpleGUI.WIN_CLOSED:
        break

window.close()