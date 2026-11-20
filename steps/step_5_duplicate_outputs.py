# Step 5: two callbacks that update the same output.
# New in this step: a Reset button and allow_duplicate=True.
# Run from the repo root:  python steps/step_5_duplicate_outputs.py
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, assets_folder="../assets", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Div([
            html.H1("Hello, World!"),
            html.P("This is my first Dash app."),
        ]),
        html.Div(
            [
                dbc.Button("Click me please", id="button"),
                dbc.Button("Reset", id="reset-button", color="secondary"),
                dcc.Input(id="input", type="text", placeholder="Write something"),
                dbc.Card(id="card", children="Button not clicked yet"),
            ],
            className="stack",
        ),
    ],
    className="page",
)


@callback(
    Output("card", "children"),
    Input("button", "n_clicks"),
    State("input", "value"),
    prevent_initial_call=True,
)
def update_card(n_clicks, text):
    return f"Button clicked {n_clicks} times and I wrote {text}"


# By default, each Output can belong to only ONE callback. Remove
# allow_duplicate=True below and Dash shows a "Duplicate callback outputs" error.
#
# allow_duplicate=True lets a second callback write to the same output.
# Dash requires prevent_initial_call=True with it, otherwise both callbacks
# would race to set the card when the page loads.
@callback(
    Output("card", "children", allow_duplicate=True),
    Input("reset-button", "n_clicks"),
    prevent_initial_call=True,
)
def reset_card(n_clicks):
    return "Button not clicked yet"

# The other way to do this is ONE callback with both buttons as Inputs,
# using dash.ctx.triggered_id to see which button was clicked:
#
#     if ctx.triggered_id == "reset-button":
#         return "Button not clicked yet"


if __name__ == "__main__":
    app.run(debug=True)
