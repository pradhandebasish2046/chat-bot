import chainlit as cl
import pandas as pd
from src.llm import ask_order, messages


@cl.on_chat_start
async def start():
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!", accept=[".csv"]
        ).send()

    text_file = files[0]
    path = text_file.path
    df = pd.read_csv(path)

    # Let the user know that the system is ready
    response = ask_order(messages)  # Generated Code
    with open('output_script.py', 'w') as f:
        f.write(response)  # Storing generated code in a .py file
    await cl.Message(
        content=f"`{text_file.name}` uploaded, it contains {df.shape} characters! and response is {response}"
    ).send()
