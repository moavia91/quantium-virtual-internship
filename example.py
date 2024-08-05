import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Region Selector'),

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

    html.Div(id='selected-region')
])

# Define callback to update text based on selected region
@app.callback(
    Output('selected-region', 'children'),
    [Input('region-selector', 'value')]
)
def update_text(selected_region):
    return f'You have selected: {selected_region}'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
