import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('/Users/muhammadmoavia/Desktop/Quantium Program/quantium-virtual-internship/final_sales.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort data by date
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Sales Data Visualizer'),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(df, x='date', y='sales', title='Sales Over Time', labels={'date': 'Date', 'sales': 'Sales'})
    ),

    html.Div(id='price-increase-analysis')
])


# Define callback to update analysis text

def update_analysis(figure):
    before_increase = df[df['date'] < '2021-01-15']['sales'].sum()
    after_increase = df[df['date'] >= '2021-01-15']['sales'].sum()
    if before_increase > after_increase:
        return 'Sales were higher before the price increase on January 15, 2021.'
    else:
        return 'Sales were higher after the price increase on January 15, 2021.'


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
