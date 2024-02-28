from openai import OpenAI
from src.prompt import user_instruction

client = OpenAI()
# prompt = "What are total no of nan values present in the column age"
messages = [
    {"role": "system", "content": "You are a helpful assistant who will help to genearate python code."},
    {"role": "user", "content": f"Assume a pandas dataframe which is stored in a variable'df'.Now generate the code for the below task.\
     \n{user_instruction}. Give me only the python code and necessary libraries that we want to import.\
     Do not return explanations or comments because your generated code will automatically executed in a python file.\
        So please avoid any bugs or texts that may create any error"},
]


def ask_order(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content
