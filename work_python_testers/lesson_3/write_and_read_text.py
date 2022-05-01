def write_text(file_name,lines):
    my_file = open(file_name, "a")
    my_file.writelines(lines)
    my_file.close()

def file_read(file_name):
    result = []
    my_file = open(file_name, "r")
    result = my_file.read()
    my_file.close()
    return result


