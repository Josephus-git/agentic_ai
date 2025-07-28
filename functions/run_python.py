import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    """
    Executes a Python file within a specified working directory.

    Args:
        working_directory (str): The permitted working directory.
        file_path (str): The path to the Python file to execute.
        args (list): A list of additional arguments to pass to the Python script.

    Returns:
        str: The formatted output of the execution, an error message, or a timeout message.
    """
    try:
        working_abs_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abs_file_path = os.path.abspath(full_path)

        # 1. Check if file_path is within working_directory
        # os.path.commonpath returns the longest path that is a prefix of all paths in the sequence
        # If commonpath of (working_directory, file_path) is not working_directory,
        # then file_path is outside working_directory.
        # Validate that the full_path stays within the working_directory boundaries
        if not abs_file_path.startswith(os.path.abspath(working_abs_path)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        

        # 2. Check if the file exists
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        # 3. Check if the file ends with ".py"
        if not file_path.lower().endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Construct the command
        command = ["python", abs_file_path] + args

        # Execute the Python file
        try:
            completed_process = subprocess.run(
                command,
                cwd=working_abs_path,
                capture_output=True,
                text=True,  # Decode stdout/stderr as text
                timeout=30  # 30-second timeout
            )
        except subprocess.TimeoutExpired:
            return f"Error: Execution of \"{file_path}\" timed out after 30 seconds."
        except FileNotFoundError:
            return "Error: Python interpreter not found. Ensure Python is installed and in your PATH."

        stdout_output = completed_process.stdout.strip()
        stderr_output = completed_process.stderr.strip()
        return_code = completed_process.returncode

        output_parts = []

        if stdout_output:
            output_parts.append(f"STDOUT:\n{stdout_output}")
        if stderr_output:
            output_parts.append(f"STDERR:\n{stderr_output}")

        if return_code != 0:
            output_parts.append(f"Process exited with code {return_code}")

        if not output_parts:
            return "No output produced."
        else:
            return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"