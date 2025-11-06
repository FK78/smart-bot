import os

def write_file(working_directory, file_path, content):
    if file_path.startswith("/") or file_path.startswith("../"):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.file_path.exists:
        os.makedirs
    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"