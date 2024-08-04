import pandas as pd
import glob
import os


def process_csv(file_path):
    df = pd.read_csv(file_path)

    df_filtered = df[df['product'] == 'pink morsel']

    df_filtered['quantity'] = pd.to_numeric(df_filtered['quantity'], errors='coerce')
    df_filtered['price'] = pd.to_numeric(df_filtered['price'].str.replace('$', ''), errors='coerce')

    df_filtered['sales'] = df_filtered['quantity'] * df_filtered['price']

    result_df = df_filtered[['sales', 'date', 'region']]

    return result_df


# List CSV File Paths

csv_files = ['/Users/muhammadmoavia/Desktop/Quantium Program/quantium-virtual-internship/data/daily_sales_data_0.csv', '/Users/muhammadmoavia/Desktop/Quantium Program/quantium-virtual-internship/data/daily_sales_data_1.csv', '/Users/muhammadmoavia/Desktop/Quantium Program/quantium-virtual-internship/data/daily_sales_data_2.csv']

final_df = pd.concat([process_csv(file) for file in csv_files])

final_df.to_csv('final_sales.csv', index=False)

print("Data has been processed and saved to 'final_sales.csv'.")
