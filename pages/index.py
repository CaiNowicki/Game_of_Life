import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
from app_scripts.game_objects import Grid
from app_scripts.interface import create_grid
from app import app
grid = Grid(25)
game = create_grid(25, grid)

column1 = dbc.Col(
    [
        dcc.Markdown("""John Conway's Game of Life
           Created in Python using Plotly-dash
            """
                     ),
        dcc.Graph(figure=game),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds
            n_intervals=0
        )
    ],
    md=4,
)

layout = dbc.Row([column1])


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_grid_live(n):
    grid = Grid(25)
    game = create_grid(25, grid)
    while n < 100:
        create_grid(25, grid)
        grid.update_grid()
