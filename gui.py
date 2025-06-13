import functions
import FreeSimpleGUI as sg
import time

sg.theme("Topanga")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do:", key="todo")

# Adding an image file to buttons
# add_button = sg.Button(image_source="add.png", tooltip='Add',
# image_size=(25,25), mouseover_colors="LightBlue2", key="Add")

add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 15])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

button_labels = ["Close", "Apply"]

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d-%b-%Y %H:%M:%S"))

    match event:
        case sg.WIN_CLOSED:
            break

        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                # Fix break-line bug
                if not new_todo.endswith('\n'):
                    new_todo = new_todo + '\n'
                #
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 14))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 14))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

window.close()

