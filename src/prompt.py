from src.constants import uploaded_file_location


def generate_instruction(user_msg, header_details, uploaded_file_location):
    instruction = f"""Act like a coding Assistant and Generate the code step by step.\n
### STEP 1 ###
Start by reading the file location from {uploaded_file_location} and read the csv file. Use below code\n
file_location = open({uploaded_file_location}, 'r').readline().strip()
df = pd.read_csv(file_location)
### STEP 2 ###
Now in second step read the below instruction properly and generate bug free executable python code.
###
{user_msg}.\n###
Below is the name of the headers and their data types of the given dataframe\n{header_details}\n
Provide only the Python code along with the necessary libraries to import.
If the user requests plots, save the plot instead of displaying it. 
Avoid including explanations or comments in the returned code.
Do not give backticks in start or end of the code. 
"""
    print(instruction)
    return instruction


def generate_instruction_again(user_msg, header_details, error_message, generated_code):
    instruction = f"""Act like a coding assistant to resolve the possible bug in a given python code\n
Below is the name of the headers and their data types of the given dataframe\n{header_details}\n
Below is my code that I am trying to implement for the task "{user_msg}".\n
{generated_code}\n
For this code I am getting error.\n
{error_message}
Now give me the updated error free code.
Provide only the Python and avoid including explanations or comments in the returned code.
Do not give backticks in start or end of the code. 
"""
    print(instruction)
    return instruction
