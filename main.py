import os
from google import genai
from dotenv import load_dotenv
import sys
from google.genai import types
from functions.get_files_info import available_functions


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    model_name = "gemini-2.0-flash-001"

    input = sys.argv
    if len(input) < 2:
        print("usage: uv run main.py <command>")
        os._exit(1)

    user_prompt = input[1]
    verbose = False
    if len(input) > 2:
        if input[2] == "--verbose":
            verbose = True

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            ),
    )
    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    if len(response.function_calls) > 0:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else: 
        print(response.text)


if __name__ == "__main__":
    main()
