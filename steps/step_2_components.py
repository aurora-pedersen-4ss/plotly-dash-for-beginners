# Step 2: add some components.
# New in this step: a button, a text input and a card.
# Nothing happens when you click the button yet; that comes in step 3.
# Run from the repo root:  python steps/step_2_components.py
from dash import Dash, html, dcc
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
                # Every component we want to use in a callback later needs a unique id
                dbc.Button("Click me please", id="button"),
                dcc.Input(id="input", type="text", placeholder="Write something"),
                dbc.Card(id="card", children="Button not clicked yet"),
            ],
            className="stack",  # 16px between each component, see assets/style.css
        ),
    ],
    className="page",
)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
