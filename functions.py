FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = [line.strip() for line in file_local.readlines()]
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines([todo + '\n' for todo in todos_arg])


# The conditional is used when we don't want the code to
# appear when running the main app.
# Generally used to test functions while running the file directly.
if __name__ == "__main__":
    print(get_todos())

