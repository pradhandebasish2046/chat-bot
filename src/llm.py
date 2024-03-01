from openai import OpenAI
from src.utils import user_instruction
from src.prompt import generate_instruction

from src.constants import header_detail_file_location, uploaded_file_location
client = OpenAI()


def generate_prompt(user_msg, header_detail_file_location, uploaded_file_location):
    # prompt = "Give me the plot which shows the distribution of column SepalLengthCm"
    with open(header_detail_file_location, 'r') as file:
        header_details = file.read().strip()
        instruction = generate_instruction(
            user_msg, header_details, uploaded_file_location)

    return instruction


def generate_code(user_msg, header_detail_file_location, uploaded_file_location):
    instruction = generate_prompt(
        user_msg, header_detail_file_location, uploaded_file_location)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who will help to generate executable python code."},
            {"role": "user", "content": instruction},
        ]
    )

    return response.choices[0].message.content
