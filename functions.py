FILENAME = "todos.txt"


def get_todos(filepath=FILENAME):
    """Read a text file and return the to-do items as a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(list_name, filepath=FILENAME):
    """Write the items in the todos list into the text file"""
    with open (filepath, 'w') as file:
        file.writelines(list_name)
