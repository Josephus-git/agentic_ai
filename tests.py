import os
from functions.run_python import run_python_file


# --- New Test Cases for run_python_file ---

print("--- Test Case 1: Displaying calculator usage ---")
print(run_python_file("calculator", "main.py"))
print("\n")

print("--- Test Case 2: Running calculator with an expression ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("\n")

print("--- Test Case 3: Running a different Python file (calculator/tests.py) ---")
print(run_python_file("calculator", "tests.py"))
print("\n")

print("--- Test Case 4: Attempting to run a file outside the working directory (should error) ---")
print(run_python_file("calculator", "../main.py"))
print("\n")

print("--- Test Case 5: Attempting to run a nonexistent file (should error) ---")
print(run_python_file("calculator", "nonexistent.py"))
print("\n")