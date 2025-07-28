import os
from .config import MAX_CHARS

def get_files_info(working_directory, directory="."):
    """
    Retrieves information about files and directories within a specified directory,
    ensuring it stays within the working_directory boundaries.

    Args:
        working_directory (str): The absolute path to the permitted working directory.
        directory (str): The relative path to the directory to list within
                         the working_directory. Defaults to ".".

    Returns:
        str: A string representing the contents of the directory in a specific format,
             or an error message if the directory is outside boundaries or not a directory.
    """
    try:
        full_path = os.path.join(working_directory, directory)
        full_path = os.path.abspath(full_path)

        # Validate that the full_path stays within the working_directory boundaries
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        items_info = []
        for item_name in os.listdir(full_path):
            item_path = os.path.join(full_path, item_name)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path) if not is_dir else 0  # Size of directory not strictly needed for this problem

            items_info.append(f"- {item_name}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(items_info)
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"
    

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

        
        
