import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from app_scripts.game_objects import Grid
from app_scripts.interface import create_interactive_grid
from app import app

grid = Grid(n=25)
game = create_interactive_grid(25, grid)


column1 = dbc.Col(
    [
        dcc.Markdown(
            """

           ##John Conway's Game of Life
            """
        ),
        dcc.Graph(figure=game)
    ]
)

layout = dbc.Row([column1])
