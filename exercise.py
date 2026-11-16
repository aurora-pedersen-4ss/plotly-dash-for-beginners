from dash import Dash, State, html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go

# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define what the page looks like
app.layout = html.Div(
    [
        # Add your components here
    ],
    className="page",  # page gutter + 24px between each child, see assets/style.css
)

# Add your callbacks here


# Start the development server
if __name__ == "__main__":
    app.run(debug=True)
