from dotenv import load_dotenv
import streamlit as st
import requests
from openai import OpenAI
import json



# Function to get a fun fact about a number from numbersapi.com
def get_number_fun_fact(num: str) -> str:
    """Calls numbersapi.com/{num}/math API using the inputted number and returns a fun fact about that number."""
    response = requests.get(f"http://numbersapi.com/{num}/math")
    if response.ok:
        return response.text
    else:
        return "Failed to retrieve fun fact."

# Function to call GPT model with functions
def call_gpt_with_functions(input: str) -> str:
    # Load environment variables
    load_dotenv()

    # Initialize OpenAI client
    client = OpenAI()

    # Define the system and user messages
    messages = [
        {
            "role": "system",
            "content": """
            You are an advanced assistant designed to provide users with a fun fact about a number included in their input, {input}. 
            Utilize the numbersapi.com API to retrieve these fun facts. Ensure that you only relay the fun facts obtained directly from the numbersapi.com API, without creating your own facts or altering the content. Do not provide any output other than the fun fact, and do not format the response in JSON. If the user's input does not contain a number, inform them that you can provide a fun fact if they specify a number. It is acceptable if the input includes additional text, as long as a number is present. If a number is included but it is not a positive integer or 0 (zero), notify the user that you only provide fun facts for positive integers.
            """,
        },
        {
            "role": "user",
            "content": input,
        }
    ]
    
    # Create a chat completion with the GPT model
    response = client.chat.completions.create(
        model='gpt-4',
        messages=messages,
        functions=[
            {
                "name": "get_number_fun_fact",
                "description": "Calls numbersapi.com API using the inputted number and returns a fun fact about that number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num": {
                            "type": "string",
                            "description": "The number which will be used in the API call to numbersapi.com to get a fun fact about it",
                        },
                    },
                    "required": ["num"],
                }
            }
        ],
        function_call="auto"
    )
    
    # Check if the function was called
    use_function = response.choices[0].finish_reason == "function_call"
    content = ""
    
    # If the function was called, get the fun fact and append it to the messages
    if use_function and response.choices[0].message.function_call.name == "get_number_fun_fact":
        arguments = json.loads(response.choices[0].message.function_call.arguments)
        content = get_number_fun_fact(arguments['num'])
        messages.append(response.choices[0].message)
        messages.append({
            "role": "function",
            "name": "get_number_fun_fact", 
            "content": content,
        })
    
    # Create a final chat completion with the updated messages
    final_response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    
    # Return the content of the final message
    return final_response.choices[0].message.content

# Main function to run the Streamlit app
def main():
    # Set the page title and header
    st.set_page_config(page_title="Number Random Fact Generator")
    st.header("Fun Fact About a Number",divider="rainbow")
    
    # Get user input
    user_input = st.text_input("Select a number to get a fun fact about:")
    
    # If user input is provided, display it and the fun fact
    if user_input:
        st.write(f"Your input: {user_input}")
        st.write(call_gpt_with_functions(user_input))

# Run the main function if this script is the main entry point
if __name__ == "__main__":
    main()
