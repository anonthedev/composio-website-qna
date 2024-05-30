# Website QnA Assistant
This project is a web scraper and Q&A assistant that uses OpenAI's API to answer questions based on the content of a specified website. The assistant scrapes the website for text content, processes the data, and then uses OpenAI's GPT-4 model to provide answers to user queries.


## Installation
- Clone the Repository

```
git clone https://github.com/yourusername/website-qna-assistant.git
cd website-qna-assistant
```

- Install the Required Packages

```
pip install -r requirements.txt
```

- Set Up OpenAI API Key
    Create a .env file and put in your API Key
    ```
    OPENAI_API_KEY=sk-
    ```

## Usage
   - Enter the website you want to QnA with in the ```scrape_website``` function

   - Run the Script

        ```
        python main.py
        ```

    - Ask Questions

    ```
    Ask a question: How many applications does composio support? give me a number
    ```

The assistant will process your question and provide an answer.

## Exit the Program

To exit the program, press Ctrl+C.

Project Structure
main.py: The main script that scrapes the website, uploads the content to OpenAI, and handles the Q&A interaction.
requirements.txt: A list of Python packages required for the project.


Notes
Ensure your OpenAI API key has the necessary permissions and quota to create assistants and process queries.
Modify the scrape_website function if you need to scrape a different website or multiple pages.
The assistant currently uses the code_interpreter tool with GPT-4-turbo model; adjust these settings based on your needs and OpenAI's available features.