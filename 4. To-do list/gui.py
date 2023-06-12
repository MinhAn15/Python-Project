import module.function
import PySimpleGUI

label = PySimpleGUI.Text("Type in a todo")
input_box = PySimpleGUI.InputText(tooltip="Enter todo ")
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("Andy's Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()