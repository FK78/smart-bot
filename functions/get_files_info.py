import os

def get_files_info(working_directory, directory="."):
    joined_path = os.path.join(working_directory, directory)
    if directory == ".":
        string = "Result for current directory:\n"
    else:
        string = f"Result for {directory} directory:\n"
    if directory.startswith("/") or directory.startswith("../"):
        string += f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return string
    if not os.path.isdir(joined_path):
        string += f'Error: "{directory}" is not a directory'
        return string
    try:
        for file in os.listdir(joined_path):
            full_path = os.path.join(joined_path, file)
            string = string + (f"- {file}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}\n")
        return string
    except Exception as e:
        return f"Error: {str(e)}"