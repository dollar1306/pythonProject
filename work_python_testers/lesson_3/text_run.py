from work_python_testers.lesson_3.write_and_read_text import write_text, file_read

lines = ["\nhello world\n", "how are you today\n", "zaebal yakir, mafriya\n"]
file_name = "myText.txt"
write_text(file_name, lines)
result = file_read(file_name)
print(result)
