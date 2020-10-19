import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app_scripts.game_objects import Grid
from app_scripts.interface import create_grid
import time


grid = Grid(10)
game = create_grid(5, grid)

meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]
external_stylesheets = [dbc.themes.SPACELAB]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = "Conway's Game of Life"
server = app.server

grid = Grid(25)
grid = create_grid(25, grid)

app.layout = html.Div(
    html.Div([
        html.H1("John Conway's Game of Life"),
        html.Div("Written in Python using Plotly-Dash"),
        html.Iframe(srcDoc= open(r'C:\Users\caino\PycharmProjects\compsci\Game_of_Life\iframe_figures\figure_0.html', 'r').read()),
        dcc.Interval(id='interval-component', interval=10, n_intervals=0),
        html.Div(grid.generation)
    ])
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def reload_page():
    time.sleep(0.5)
    return app.layout

if __name__ == '__main__':
    app.run_server(debug=True)
