import os
from functions.get_files_info import get_file_content

print("--- Running get_files_content tests ---")

# Test Case 1: get_files_content("calculator", "main.py")
print("\nget_files_content('calculator', 'main.py')")
result1 = get_file_content("calculator", "main.py")
print("Result for main.py")
print(result1)

# Test Case 2: get_files_content("calculator", "pkg")
print("\nget_files_content('calculator', 'pkg/calculator.py')")
result2 = get_file_content("calculator", "pkg/calculator.py")
print("Result for 'pkg/calculator.py'")
print(result2)

# Test Case 3: get_files_content("calculator", "/bin.cat")
print("\nget_files_content('calculator', '/bin/cat')")
result3 = get_file_content("calculator", "/bin/cat")
print("Result for '/bin/cat'")
print(result3)

# Test Case 4: get_files_info("calculator", "pkg/does_not_exist.py")
print("\nget_files_content('calculator', 'pkg/does_not_exist.py')")
result4 = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for 'pkg/doesnotexist'")
print(result4)