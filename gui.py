import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("darkgrey4")

time_label = sg.Text(" ",key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo",key='todo')
list_box = sg.Listbox(values=functions.get_todos(),key='todos', #The key todos is used to refer the listbox later on if we need it
                      enable_events=True, size=[45, 10])        #The values takes a list as a argument in the Listbox
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Todo Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-do App',
                   layout=[[time_label],[label],[input_box,add_button],[list_box,edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%d %b, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) #by window['todos'] we mean the listbox and its key is todos
        case 'Edit':
            try:
                todo_to_edit = values["todos"][0]
                # When you select a todo you can see that the todo is stored in the todos key by print(values)
                # Because of [0] we will only get the string
                new_todo = values['todo'] + "\n" #instead of the list

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                #updating the list after editing the todo
                window['todos'].update(values=todos) #values - for list,#value for string/argument
            except IndexError:
                sg.popup('First select a todo before clicking the Edit button',font=('Helvetica', 20))

        case 'todos':
            #updating the todo in the search bar when we select a todo to that todo
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup('First select a todo before clicking the Complete button',font=('Helvetica', 20))

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
