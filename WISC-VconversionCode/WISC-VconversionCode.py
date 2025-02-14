# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:03:31 2025
This file converts the raw scores obtained from WISC-V 
@author: Liu
"""

import pandas as pd



def determine_table(a, b, x):
    # Constrain values to defined ranges
    a = min(max(a, 7), 11)
    if b <= 3:
        b_range = 0
    elif b <= 6:
        b_range = 1
    elif b <= 9:
        b_range = 2
    else:
        b_range = 3

    return conversion_tables.get((a, b_range, x))

def convert_value(value, table_func):
    if table_func:
        return table_func(value)
    return None

def process_excel(file_path, output_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Filter columns: keep first two and columns ending with "(Rohwertsumme)"
    filtered_columns = [col for col in df.columns if col.endswith("(Rohwertsumme)") or col in df.columns[:2]]
    df = df[filtered_columns]

    # Identify the correct 4 columns based on first character (4,5,9,10)
    score_columns = [col for col in filtered_columns[2:] if col[0] in ('4', '5', '9', '10')]
    if len(score_columns) != 4:
        raise ValueError("Expected exactly 4 score columns, but found {}".format(len(score_columns)))
        
     

    # Process each row
    result_data = {df.columns[0]: df[df.columns[0]]}

    # Extract a and b from the second column (format: 'a:b')
    a_b_values = df.iloc[:, 1].str.split(':', expand=True).astype(int)
    a_values = a_b_values[0]
    b_values = a_b_values[1]

    # Convert scores
    for col in score_columns:
        x = int(col[0])
        result_data[col] = [
            convert_value(val, determine_table(a, b, x))
            for val, a, b in zip(df[col], a_values, b_values)
        ]

    # Create the output dataframe and save as CSV
    output_df = pd.DataFrame(result_data)
    output_df.to_csv(output_path, index=False)

# Example usage
input_file = 'input.xlsx'
output_file = 'output.csv'
process_excel(input_file, output_file)
print(f"Processed file saved to {output_file}")")
    }
  ]
}
