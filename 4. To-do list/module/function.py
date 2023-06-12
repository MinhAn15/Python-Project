def read_todos(file_path):
    with open(file_path, 'r', encoding= 'utf-8') as file_read:
        todos =  file_read.readlines()
    return todos
def write_todos(file_path, todos):
    with open(file_path, 'w', encoding= 'utf-8') as file_write:
        file_write.writelines(todos)
    return

if __name__ == '__main__':
    print("Hello")