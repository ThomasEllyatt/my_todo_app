def view_existing_todo_lists():
    import os

    # folder path
    dir_path = os.getcwd()

    # list file and directories
    for path in os.scandir(dir_path):
        if path.is_file() and 'txt' in path.name:
            print(path.name[:-4])


def create_todo_list(name):
    import os

    dir_path = os.getcwd()
    try:
        with open(f"{dir_path}/{name}.txt", 'x') as fp:
            pass
    except FileExistsError:
        print('File already exists')
    active_list = f"{name}.txt"
    return active_list


def get_todos(filename):
    with open(f"{filename}", 'r') as file:
        data = file.readlines()
    return data


def update_todo(filename, todos):
    with open(f"{filename}", 'w') as file:
        todos = [x.capitalize() for x in todos]
        todos.sort()
        file.writelines(todos)
    return todos


def print_todos(filename):
    todos = get_todos(filename)
    print(f"Showing tasks within the '{filename}' todo list:")
    for index, item in enumerate(todos, start=1):
        row = f"{index}. {item}"
        print(row.strip("\n"))
    filename = f"{filename}"
    return filename
