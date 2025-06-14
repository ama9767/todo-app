import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"].strip()
    if todo_local:  # only add if not empty
        todos.append(todo_local)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # clear input box

st.title("My Todo App")
st.write("This app is to increase your productivity.")

# Display todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Input box for new item
st.text_input(label="New Todo",
              label_visibility="collapsed",
              placeholder= "Add new todo..",
              on_change=add_todo, key='new_todo')

# Clear All button with confirmation
with st.expander("Clear All Todos"):
    st.warning("This will delete all your todos permanently!")
    if st.button("Yes, clear all"):
        todos.clear()
        functions.write_todos(todos)
        # Reset session_state keys for checkboxes
        for key in list(st.session_state.keys()):
            if key != 'new_todo':
                del st.session_state[key]
                st.rerun()