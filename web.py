import functions
import streamlit as st


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My to do App")
st.subheader("This is my to do app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a Todo", placeholder="Enter a new todo to add: ",
              on_change=add_todo, key='new_todo')
