import streamlit as st
import todo_functions
# import os


def add_todo_local():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    todo_functions.update_todo(filename, todos)
    return todos


# dir_path = os.path.dirname(os.path.realpath(__file__))
# filename = f'{dir_path}\\todos.txt'
filename = "todos.txt"
todos = todo_functions.get_todos(filename)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
# st.snow()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        todo_functions.update_todo(filename, todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ",
              placeholder="Add a new todo...",
              on_change=add_todo_local,
              key="new_todo",
              value="")

st.session_state
