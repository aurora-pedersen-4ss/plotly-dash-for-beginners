# Step 3: make the page react with a callback.
# New in this step: @callback with an Input and an Output.
# Clicking the button now updates the text in the card.
# Run from the repo root:  python steps/step_3_callback.py
from dash import Dash, html, dcc, callback, Input, Output
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
                dcc.Input(id="input", type="text", placeholder="Write something"),
                dbc.Card(id="card", children="Button not clicked yet"),
            ],
            className="stack",
        ),
    ],
    className="page",
)


# A callback connects components:
#   Output(component_id, property): what the function's return value updates
#   Input(component_id, property):  what triggers the function when it changes
# Here: when the button's n_clicks changes, update the card's children (its content).
@callback(
    Output("card", "children"),
    Input("button", "n_clicks"),
)
def update_card(n_clicks):
    # Note: this also runs once when the page loads, with n_clicks = None.
    # Step 4 shows how to skip that first call.
    return f"Button clicked {n_clicks} times"


if __name__ == "__main__":
    app.run(debug=True, port=5050)
