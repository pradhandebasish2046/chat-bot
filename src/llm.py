from openai import OpenAI
from src.utils import user_instruction
from src.prompt import generate_instruction, generate_instruction_again

from src.constants import header_detail_file_location, uploaded_file_location
client = OpenAI()


def generate_prompt(user_msg, header_detail_file_location, uploaded_file_location):
    with open(header_detail_file_location, 'r') as file:
        header_details = file.read().strip()
        instruction = generate_instruction(
            user_msg, header_details, uploaded_file_location)

    return instruction


def generate_prompt_again(user_msg, header_detail_file_location, generated_code, error_msg):
    with open(header_detail_file_location, 'r') as file:
        header_details = file.read().strip()
        instruction = generate_instruction_again(
            user_msg, header_details, generated_code, error_msg)

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


def generate_code_again(user_msg, header_detail_file_location, generated_code, error_msg):
    instruction = generate_prompt_again(
        user_msg, header_detail_file_location, error_msg, generated_code)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who will help to generate executable python code."},
            {"role": "user", "content": instruction},
        ]
    )
    print(instruction)
    return response.choices[0].message.content
