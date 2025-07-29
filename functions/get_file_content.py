import os
from .config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(full_path)

    # Validate that the full_path stays within the working_directory boundaries
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{full_path}"'
    
    try:
        with open(full_path, "r") as f:
            full_content = f.read()

        if len(full_content) > MAX_CHARS:
            file_content_string = full_content[:MAX_CHARS] + f"[...File \"{full_path}\" truncated at {MAX_CHARS} characters]"
        else:
            file_content_string = full_content

    except FileNotFoundError:
        return f"Error: File not found at '{full_path}'"

    except Exception as e:
        return f"Error reading file '{full_path}': {e}"

    return file_content_string
