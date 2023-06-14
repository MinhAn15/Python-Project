import streamlit as st
import module.function as f

todos = f.read_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    f.write_todos(todos)

todos = f.read_todos()
st.title("An's Todo App")
st.subheader("List your todo below")
st.write("This app help improving your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    
st.text_input(label="", placeholder="Enter your idea"
              , on_change=add_todo, key='new_todo')