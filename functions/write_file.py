import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_path = os.path.abspath(full_path)

        # Validate that the full_path stays within the working_directory boundaries
        if not abs_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{abs_path}" as it is outside the permitted working directory'
        
        # Ensure the directory for the file exists
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        # Overwrite the contents of the file
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
    
    