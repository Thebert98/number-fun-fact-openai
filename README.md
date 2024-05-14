# Number Fun Fact Generator

This project is an interactive application that provides users with fun facts about numbers. It utilizes the numbersapi.com API to fetch real-time data and employs OpenAI GPT models for enhanced responses.

## Getting Started

1. **Clone the repository**: Clone this repository to your local machine.
2. **API Key**: You will need an OpenAI API key to interact with the GPT models. Follow the instructions below to set it up.

### Setting Up Your OpenAI API Key

1. If you haven't already, sign up for an OpenAI account and obtain an API key.
2. Copy the `.env.example` file to a new file named `.env`.
3. Replace the placeholder in the `.env` file with your actual OpenAI API key.

## Installation

Before running the application, make sure you have Python installed on your system. Then, follow these steps to install the necessary dependencies:

1. Navigate to the project directory.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On MacOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, use the following command in the project directory:

```bash
streamlit run main.py
```

This will start the Streamlit server and open the application in your default web browser. You can then interact with the application to obtain fun facts about numbers.

## Features

- **Interactive Input**: Enter a number or a sentence containing a number to learn a fun fact about it.
- **Live API Interaction**: Utilizes numbersapi.com to fetch real-time data.
- **LLM Integration**: Employs OpenAI GPT models for enhanced responses.

## Input Handling

The application can handle both plain numbers and natural language inputs containing numbers. For example:

- Direct number input: `5`
- Natural language input: `Tell me something interesting about the number 5.`

The application will extract the number from the input and provide a fun fact about it. If the input does not contain a number or contains an invalid number, the user will be informed accordingly.
