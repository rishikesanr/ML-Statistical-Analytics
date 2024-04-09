import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Assume 'df' is your DataFrame loaded from 'final.xlsx'
# df = pd.read_excel('/path/to/final.xlsx')

# Example DataFrame loading (adjust according to your real dataset)
df = pd.DataFrame({
    'Condition': ['Changing Lanes', 'Entering Traffic', 'Others', 'Passing Other Vehicle'],
    'Odds': [1.2485, 1.1630, 1.7061, 1.6744]
})

# Example Plotly Express chart
fig = px.bar(df, x='Condition', y='Odds', title='Odds of Severe Injury for Different Conditions')

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='San Francisco Road Safety Dashboard'),

    html.Div(children='''
        San Francisco Real Time Traffic Accidents Contributors.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
