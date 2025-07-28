import os
from google import genai
from dotenv import load_dotenv
import sys
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    input = sys.argv
    if len(input) < 2:
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
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
