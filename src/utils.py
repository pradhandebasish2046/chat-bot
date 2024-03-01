import os
import pandas as pd
from src.constants import header_detail_file_location

user_instruction = """
What are total no of nan values present in the column age
"""


def generate_default_output(df):
    shape = df.shape
    missing_counts = df.isna().sum().sum()
    column_names = ""
    for col in df.columns:
        column_names += col
        column_names += ','
    no_of_duplicate_rows = df.duplicated().sum()
    txt = f"""From the given data that uploaded I found below things\n
Shape of the data:[{shape[0]},{shape[1]}].\n
Total Missing values:\n {missing_counts}\n
Column_name: {column_names[:-1]}\n
Duplicate Rows: {no_of_duplicate_rows}"""
    return txt


def dataframe_header_details(df, header_detail_file_location):
    if os.path.exists(header_detail_file_location):
        # If it exists, delete the file
        os.remove(header_detail_file_location)
    with open(header_detail_file_location, 'w') as f:
        for key, value in df.dtypes.to_dict().items():
            f.write(f"{key}:{value}\n")
