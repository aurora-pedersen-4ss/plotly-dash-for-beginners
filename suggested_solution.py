from dash import Dash, State, html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go

FUNCTIONS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
}

def input_button_group(label, default_val):
    # Create an input group for a parameter with a label and default value
    return dbc.InputGroup([
        dbc.InputGroupText(label),
        dbc.Input(id=f"param-{label}", value=default_val, type="number"),
    ])

def compute_trig(func, a, b, c, d, x):
    # Compute the trigonometric function with the given parameters and input array x
    if func in FUNCTIONS.values():
        return a * func(b * x + c) + d
    return None

# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define what the page looks like
app.layout = html.Div(
    [
        html.Div([
            html.H1("This is my trigonometry app!"),
            html.P("Explore trigonometric functions and their properties."),
        ]),
        dbc.Row(children=[ # This arranges the inputs in one row instead of stacking them vertically
            dbc.Col(
                dcc.Dropdown(id="function-dropdown", options=[
                    {"label": "sin", "value": "sin"},
                    {"label": "cos", "value": "cos"},
                    {"label": "tan", "value": "tan"}
                ], value="sin")),
            dbc.Col(input_button_group("a", 1)),
            dbc.Col(input_button_group("b", 1)),
            dbc.Col(input_button_group("c", 0)),
            dbc.Col(input_button_group("d", 0)),
            dbc.Col(dbc.Button("Calculate", id="calculate-btn"))
        ]),
        html.Div(dcc.Graph(id="trig-graph"))
    ],
    className="page",  # page gutter + 24px between each child div, see assets/style.css
)


@callback(
    Output("trig-graph", "figure"),
    Input("calculate-btn", "n_clicks"),
    State("function-dropdown", "value"),
    State("param-a", "value"),
    State("param-b", "value"),
    State("param-c", "value"),
    State("param-d", "value"),
)
def calculate(n_clicks, func, a, b, c, d):
    fig = go.Figure()
    
    if func in FUNCTIONS:
        func = FUNCTIONS[func]
    
    x = np.linspace(-10, 10, 400)
    y = compute_trig(func, a, b, c, d, x)
    title = f"f(x) = {a} * {func.__name__}({b} * x + {c}) + {d}"

    fig.update_layout(title=title)
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))

    return fig

# Start the development server
if __name__ == "__main__":
    app.run(debug=True)
