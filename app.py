import chainlit as cl
import pandas as pd
from src.llm import generate_code
from src.utils import generate_default_output, dataframe_header_details, remove_img
import subprocess
import os
import sys

from src.constants import header_detail_file_location, uploaded_file_location
# print(os.getcwd())


@cl.on_chat_start
async def start():
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!", accept=[".csv"]
        ).send()

    uploaded_file = files[0]
    path = uploaded_file.path
    # user_message = await cl.AskTextMessage(content="Please enter your additional message:").send()

    if os.path.exists(uploaded_file_location):
        # If it exists, delete the file
        os.remove(uploaded_file_location)
    with open(uploaded_file_location, 'w') as f:
        f.write(path)

    remove_img()
    df = pd.read_csv(path)
    default_output = generate_default_output(df)
    dataframe_header_details(df, header_detail_file_location)
    await cl.Message(
        content=default_output
    ).send()


@cl.on_message
async def main(message: cl.Message):
    # Let the user know that the system is ready
    print("********", message.content)
    print(type(message.content))
    response = generate_code(
        message.content, header_detail_file_location, uploaded_file_location)  # Generated Code
    if os.path.exists('output_script.py'):
        # If it exists, delete the file
        os.remove('output_script.py')
    with open('output_script.py', 'w') as f:
        f.write(response)  # Storing generated code in a .py file
    remove_img()
    # Execute output_script.py
    python_interpreter = sys.executable
    subprocess.run([python_interpreter, 'output_script.py'])
    # subprocess.run(["python", "output_script.py"])
    # subprocess.run([sys.executable, "-m", ".venv/bin/activate","&&", "python", "output_script.py"], shell=True)
    image_extensions = ('.png', '.jpg', '.jpeg')
    all_files = os.listdir(os.getcwd())
    image_files = [
        file for file in all_files if file.lower().endswith(image_extensions)]
    for img in image_files:
        image = cl.Image(path=img, name="image1", display="inline")

        # Attach the image to the message
        await cl.Message(
            content="Please check the below Image",
            elements=[image],
        ).send()
