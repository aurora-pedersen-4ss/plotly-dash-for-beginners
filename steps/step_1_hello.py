# Step 1: the smallest possible Dash app.
# Run from the repo root:  python steps/step_1_hello.py
from dash import Dash, html
import dash_bootstrap_components as dbc

# Create the Dash app.
# assets_folder points at the shared assets/ folder in the repo root,
# so assets/style.css is loaded automatically.
app = Dash(__name__, assets_folder="../assets", external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define what the page looks like
app.layout = html.Div(
    [
        html.Div([
            html.H1("Hello, World!"),
            html.P("This is my first Dash app."),
        ]),
    ],
    className="page",  # page gutter + 24px between each child div, see assets/style.css
)

# Start the development server
if __name__ == "__main__":
    app.run(debug=True)
