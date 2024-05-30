# Website QnA Assistant
This project is a web scraper and Q&A assistant that uses OpenAI's API to answer questions based on the content of a specified website. The assistant scrapes the website for text content, processes the data, and then uses OpenAI's GPT-4 model to provide answers to user queries.


## Installation
- Clone the Repository

    ```
    git clone https://github.com/yourusername/website-qna-assistant.git
    cd website-qna-assistant
    ```

- Setup a virtual env
    ```
    python3 -m venv env
    source env/bin/activate
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
