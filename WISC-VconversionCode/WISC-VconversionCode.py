# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:03:31 2025
This file converts the raw scores obtained from WISC-V 
@author: Liu
"""

import pandas as pd

from conversion_table_new import conversion_tables  # Directly import the dictionary


def determine_table(y, m, x):

    # Check the input
    # Check the value of y and restrict m accordingly
    if y in [8, 9, 10]:
        # For y = 8, 9, or 10, m should be an integer from 1 to 12
        if m not in range(1, 13):  # 1 to 12 inclusive
            print(f"Invalid value for month: {m}. It should be between 1 and 12 when year is {y}.")
            y, m, x = -99, -99, -99
    elif y == 7:
        # For y = 7, m should be 8, 9, 10, or 11
        if m not in [8, 9, 10, 11]:
            print(f"Invalid value for month: {m}. It should be 8, 9, 10, or 11 when year is {y}.")
            y, m, x = -99, -99, -99
    elif y == 11:
        # For y = 11, m should be 0, 1, 2, or 3
        if m not in [0, 1, 2, 3]:
            print(f"Invalid value for month: {m}. It should be between 0, 1, 2, or 3 when year is {y}.")
            y, m, x = -99, -99, -99
    else:
        # If y doesn't match any of the specified conditions, raise an error
        print(f"Invalid value for year: {y}. It must be one of 7, 8, 9, 10, or 11.")
        y, m, x = -99, -99, -99

    # Determine month range
    if m < 4:
        m_range = 0
    elif m < 8:
        m_range = 1
    else:
        m_range = 2

    # Fetch the nested dictionary for conversion
    return conversion_tables.get((y, m_range, x), {})  # Return empty dict if key not found

def convert_value(value, lookup_dict):
    if lookup_dict:
        return lookup_dict.get(value, None)  # Return converted score or None if not found
    return None

def process_excel(file_path, output_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Filter columns: keep first two and columns ending with "(Rohwertsumme)"
    filtered_columns = [col for col in df.columns if col.endswith("(Rohwertsumme)") or col in df.columns[:2]]
    df = df[filtered_columns]

    # Identify the correct 4 columns based on first character (4,5,9,10)
    score_columns = [col for col in filtered_columns[2:] if col.startswith(('4', '5', '9', '10'))]
    if len(score_columns) != 4:
        raise ValueError("Expected exactly 4 score columns, but found {}. Columns found: {}".format(len(score_columns), score_columns))    
     

    # Process each row
    result_data = {df.columns[0]: df[df.columns[0]]}

    # Extract year and month from the second column (format: 'y:m')
    y_m_values = df.iloc[:, 1].str.split(':', expand=True).astype(int)
    y_values = y_m_values[0]
    m_values = y_m_values[1]

    # Convert scores
    for col in score_columns:
        # Get the prefix (first one or two characters) to determine x
        if col.startswith(('4', '5', '9', '10')):
            x = int(col.split('.')[0])  # Split at dot and get the first part as the prefix
        else:
            continue  # Skip columns that do not match the expected prefix
        result_data[col] = [
            convert_value(val, determine_table(y, m, x))
            for val, y, m in zip(df[col], y_values, m_values)
        ]

    # Create the output dataframe and save as CSV
    output_df = pd.DataFrame(result_data)
    # Change the ending to Wertpunkte to differentiate
    output_df.columns = [col.replace("(Rohwertsumme)", "(Wertpunkte)") for col in output_df.columns]
    output_df.to_csv(output_path, index=False)

# Example usage
input_file = 'WISC-V_raw_data.xlsx'
output_file = 'WISC-V_converted.csv'
process_excel(input_file, output_file)

