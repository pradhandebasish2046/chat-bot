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
Always remember the code that you are generating will be execute automatically in 
"""
    return instruction
