import os

from dash import Dash, State, html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go

# The app title comes from the APP_TITLE environment variable, with a default.
# Set it before running to change the heading, for example in PowerShell:
#   $env:APP_TITLE = "Wave explorer"
# When you publish the app, set APP_TITLE in the hosting service's settings.
APP_TITLE = os.environ.get("APP_TITLE", "My trigonometry app")

# ------------------------------------------------------------------
# Provided for you: the maths and the plotting. You don't need to change these.
# ------------------------------------------------------------------

FUNCTIONS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
}


def compute_trig(func, a, b, c, d, x):
    # Compute f(x) = a * func(b * x + c) + d for every value in the array x
    if func in FUNCTIONS.values():
        return a * func(b * x + c) + d
    return None


def make_figure(func_name, a, b, c, d):
    # Build the plot of f(x) = a * func(b * x + c) + d.
    # func_name is "sin", "cos" or "tan"; a, b, c, d are numbers.
    # Returns a Plotly figure you can return straight to a dcc.Graph's "figure".
    fig = go.Figure()
    if func_name not in FUNCTIONS or None in (a, b, c, d):
        return fig  # empty plot until every value is filled in

    func = FUNCTIONS[func_name]
    x = np.linspace(-10, 10, 400)
    y = compute_trig(func, a, b, c, d, x)

    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
    fig.update_layout(title=f"f(x) = {a} * {func_name}({b} * x + {c}) + {d}")
    return fig


# ------------------------------------------------------------------
# Your turn: build the layout and the callback.
# ------------------------------------------------------------------

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.H1(APP_TITLE),
        # TODO: add the components:
        #   - a dcc.Dropdown to pick "sin", "cos" or "tan"
        #   - four number inputs for a, b, c and d
        #   - a button to calculate
        #   - a dcc.Graph to show the plot
        # Tip: give every component you use in the callback a unique id.
    ],
    className="page",  # page gutter + 24px between each child div, see assets/style.css
)


# TODO: add a callback that runs when the button is clicked,
# reads the dropdown and the four inputs (State),
# and returns make_figure(...) to the graph's "figure" property.


# Start the development server
if __name__ == "__main__":
    # set debug=False, host="0.0.0.0" and port=5050 for production
    app.run(debug=True, port=5050)
