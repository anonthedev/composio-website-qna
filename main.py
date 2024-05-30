import requests
import os
import dotenv
from flask import request, Flask, jsonify
from bs4 import BeautifulSoup
from openai import OpenAI, OpenAIError
from flask_cors import CORS, cross_origin

dotenv.load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def remove_tags(html: str) -> str:
    """
    Remove specific HTML tags from the given HTML string.

    Args:
        html (str): The HTML string to be cleaned.

    Returns:
        str: The cleaned HTML string with specified tags removed.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["style", "script", "svg", "path", "clipboard-copy"]):
        tag.decompose()
    return " ".join(soup.stripped_strings)

def scrape_website():
    """
    Scrape a website and its subpages for text content.

    Returns:
        List[str]: A list of cleaned text content from the website and its subpages.
    """
    content = []
    reqs = requests.get("https://composio.dev")
    content.append(remove_tags(reqs.content))
    
    cleaned_content = "\n".join(content)
    # competitor_info = get_info(cleaned_content)
    file_path = "sample_text_file.txt"

    # # Write the content to the file
    with open(file_path, "w") as file:
        file.write(cleaned_content)
    return cleaned_content


scrape_website()
uploaded_file = client.files.create(
    file=open("./sample_text_file.txt", 'rb'),
    purpose='assistants',
)

retrieved_file = client.files.retrieve(uploaded_file.id)

assistant = client.beta.assistants.create(
    name="Website QnA Assistent",
    instructions="You are a AI Assistent that answers any queries related to the content provided",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo",
    tool_resources={"code_interpreter": {"file_ids": [retrieved_file.id]}},
)

thread = client.beta.threads.create()

while True:
    try:
        question = input("Ask a question: ")
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"{question} Answer according to the file provided to you. The file would be in .txt format."
        )

        run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
        )

        while True:
            try:
                run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
                print(run.status)
                if run.status=="completed":
                    print(run.status)
                    messages = client.beta.threads.messages.list(thread_id=thread.id)
                    latest_message = messages.data[0]
                    text = latest_message.content[0].text.value
                    print(text)
                    break;
            except OpenAIError:
                print("We demanded too much of OpenAI, try again.")
                break;
    except KeyboardInterrupt:
        print("Exiting...")
        break;