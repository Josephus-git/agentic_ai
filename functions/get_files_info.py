import os
import google.genai.types as types

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
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="gets file content in the specified file path",
    parameters=types.Schema(
    type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to get file content from relative to the working directory. If not provided, gets file in the working directory itself."
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs python file in the specified file_path",
    parameters=types.Schema(
    type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to get file content from relative to the working directory. If not provided, gets file in the working directory itself."
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write file in the specified file path",
    parameters=types.Schema(
    type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get file content from relative to the working directory. If not provided, gets file in the working directory itself."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to write to file."
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)        
        
