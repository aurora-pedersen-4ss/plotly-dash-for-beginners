import os

from dash import Dash, State, html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go

# The heading comes from the APP_TITLE environment variable, with a default
APP_TITLE = os.environ.get("APP_TITLE", "My trigonometry app")

FUNCTIONS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
}


def number_input(label, default_val):
    # A number input with a label in front of it, e.g. "a [ 1 ]".
    # Its id is "param-<label>", so the callback can read it.
    return dbc.InputGroup([
        dbc.InputGroupText(label),
        # We set the type to "number" so the input only accepts numeric values.
        dbc.Input(id=f"param-{label}", value=default_val, type="number"),
    ])


def compute_trig(func, a, b, c, d, x):
    # Compute the trigonometric function with the given parameters and input array x
    if func in FUNCTIONS.values():
        return a * func(b * x + c) + d
    return None


def make_figure(func_name, a, b, c, d):
    # Build the plot of f(x) = a * func(b * x + c) + d (same as in app.py)
    fig = go.Figure()
    if func_name not in FUNCTIONS or None in (a, b, c, d):
        return fig  # empty plot until every value is filled in

    func = FUNCTIONS[func_name]
    x = np.linspace(-10, 10, 400)
    y = compute_trig(func, a, b, c, d, x)

    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
    fig.update_layout(title=f"f(x) = {a} * {func_name}({b} * x + {c}) + {d}")
    return fig


# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define what the page looks like
app.layout = html.Div(
    [
        html.Div([
            html.H1(APP_TITLE),
            html.P("Explore trigonometric functions and their properties."),
        ]),
        # dbc.Row puts the inputs side by side instead of stacking them vertically
        dbc.Row([
            # list(FUNCTIONS) gives ["sin", "cos", "tan"], so the options
            # always match the functions defined above
            dbc.Col(dcc.Dropdown(id="function-dropdown", options=list(FUNCTIONS), value="sin")),
            dbc.Col(number_input("a", 1)),
            dbc.Col(number_input("b", 1)),
            dbc.Col(number_input("c", 0)),
            dbc.Col(number_input("d", 0)),
            dbc.Col(dbc.Button("Calculate", id="calculate-btn")),
        ]),
        html.Div(dcc.Graph(id="trig-graph")),
    ],
    className="page",  # page gutter + 24px between each child div, see assets/style.css
)


# No prevent_initial_call here: the callback also runs when the page loads,
# so the graph shows the default values straight away. If we didn't set the
# default values, the graph would initially be empty.
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
    return make_figure(func, a, b, c, d)


# Start the development server
if __name__ == "__main__":
    app.run(debug=True, port=5050)
