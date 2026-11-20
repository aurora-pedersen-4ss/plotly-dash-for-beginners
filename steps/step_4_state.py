# Step 4: read a value without being triggered by it.
# New in this step: State and prevent_initial_call.
# Run from the repo root:  python steps/step_4_state.py
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
                dcc.Input(id="input", type="text", placeholder="Write something"),
                dbc.Card(id="card", children="Button not clicked yet"),
            ],
            className="stack",
        ),
    ],
    className="page",
)


# State(component_id, property) passes the current value into the function,
# but changing it does NOT trigger the callback. Only the button does.
# Try swapping State for Input: the card then updates on every keystroke.
#
# prevent_initial_call=True stops the callback from running when the page loads,
# so the card keeps its "Button not clicked yet" text until the first click.
@callback(
    Output("card", "children"),
    Input("button", "n_clicks"),
    State("input", "value"),
    prevent_initial_call=True,
)
def update_card(n_clicks, text):
    # The function arguments come in the same order as the Input and State above
    return f"Button clicked {n_clicks} times and I wrote {text}"


if __name__ == "__main__":
    app.run(debug=True, port=5050)
