import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the data folder
data_folder = "data"
input_file = os.path.join(data_folder, "/Users/muhammadmoavia/Desktop/Quantium "
                                       "Program/quantium-virtual-internship/final_sales.csv")

# Load the processed data
df = pd.read_csv(input_file)

# Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Aggregate sales data by date
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['date'], daily_sales['sales'], marker='o', linestyle='-')

# Adding titles and labels
plt.title('Daily Sales of Pink Morsels Over Time')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
