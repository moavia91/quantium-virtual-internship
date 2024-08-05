# app.py

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
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

    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Default value
        labelStyle={'display': 'inline-block', 'margin-right': '10px'}
    ),

    dcc.Graph(id='sales-line-chart'),

    html.Div(id='price-increase-analysis')
])


# Define callback to update line chart and analysis text based on selected region
@app.callback(
    [Output('sales-line-chart', 'figure'),
     Output('price-increase-analysis', 'children')],
    [Input('region-selector', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create the line chart
    figure = px.line(filtered_df, x='date', y='sales', title='Sales Over Time',
                     labels={'date': 'Date', 'sales': 'Sales'})

    # Calculate sales before and after the price increase
    before_increase = filtered_df[filtered_df['date'] < '2021-01-15']['sales'].sum()
    after_increase = filtered_df[filtered_df['date'] >= '2021-01-15']['sales'].sum()

    if before_increase > after_increase:
        analysis_text = 'Sales were higher before the price increase on January 15, 2021.'
    else:
        analysis_text = 'Sales were higher after the price increase on January 15, 2021.'

    return figure, analysis_text


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
