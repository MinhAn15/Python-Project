file_path = r'D:\5. Python\Python-Project\4. To-do list\data.txt'

def read_todos(path=file_path):
    with open(path, 'r', encoding= 'utf-8') as file_read:
        todos =  file_read.readlines()
    return todos
def write_todos(todos, path=file_path):
    with open(path, 'w', encoding= 'utf-8') as file_write:
        file_write.writelines(todos)
    return

if __name__ == '__main__':
    print("Hello")