import os

def get_file_content(working_directory, file_path):
    joined_path = os.path.join(working_directory, file_path)
    if file_path == ".":
        string = "Result for current file:\n"
    else:
        string = f"Result for {file_path} file:\n"
    if not os.path.isfile(joined_path):
        string += f'Error: File not found or is not a regular file: "{file_path}"'
        return string
    if file_path.startswith("/") or file_path.startswith("../"):
        string += f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return string
    MAX_CHARS = 10000
    try:
        with open(joined_path, "r") as file:
            file_content_string = file.read(MAX_CHARS)
        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"
print(get_file_content("calculator", "lorem.txt"))