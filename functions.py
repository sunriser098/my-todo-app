FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return a list of to-do items."""
    with open(filepath, 'r') as fileread:
        todos_file = fileread.readlines()
    return todos_file


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items in the text file."""
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)
