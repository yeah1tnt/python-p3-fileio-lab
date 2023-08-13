def write_file(file_name, file_content):
    file = open(f'{file_name}.txt', 'w',encoding='utf-8')
    file.write(file_content)
    file.close()

def append_file(file_name, append_content):
    file = open(f'{file_name}.txt', 'a',encoding='utf-8')
    file.write(append_content)
    file.close()

def read_file(file_name):
    file = open(f'{file_name}.txt', 'r',encoding='utf-8')
    file_content = file.read()
    file.close()
    return file_content
