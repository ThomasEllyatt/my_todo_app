import streamlit as st
import todo_functions
# import os


def add_todo_local():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    todo_functions.update_todo(filename, todos)
    st.session_state["new_todo"] = ""
    return todos


# dir_path = os.path.dirname(os.path.realpath(__file__))
# filename = f'{dir_path}\\todos.txt'
filename = "todos.txt"
todos = todo_functions.get_todos(filename)

st.title("Tom's Tasty Tasks")
st.subheader("Le sub-header")
st.write("Put shit that needs doing down below")
# st.snow()

st.text_input(label="Enter a todo: ",
                           placeholder="Add a new todo...",
                           on_change=add_todo_local,
                           key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index} {todo}")
    new_key = f"{index} {todo}"
    if checkbox:
        print(st.session_state)
        todos.pop(index)
        todo_functions.update_todo(filename, todos)
        del st.session_state[new_key]
        del st.session_state["new_todo"]
        st.experimental_rerun()

print(st.session_state)
