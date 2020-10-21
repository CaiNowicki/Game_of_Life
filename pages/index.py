import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
from app_scripts.game_objects import Grid
from app_scripts.interface import create_grid
from app import app
from matplotlib_interactive import interactive_grid
import time

column1 = dbc.Col(
    [
        dcc.Markdown("""John Conway's Game of Life
           Created in Python using Plotly-dash
            """
                     ),
        dcc.Graph(id='game_board'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds
            n_intervals=0
        ),
        html.Button('New Game', id='reset', n_clicks=0),
        html.Button('Next', id='next', n_clicks=0),
        html.Button('Stop', id='stop', n_clicks=0)
    ],
    md=4,
)

layout = dbc.Row([column1])


@app.callback(Output('game_board', 'children'),
              [Input('reset', 'n_clicks'),
                  Input('next', 'n_clicks'),
               Input('stop', 'n_clicks')])
def update_game_board(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    points, fig= interactive_grid(25)
    grid = Grid(25)
    for point in points:
        cell = grid.__getitem__(point)
        cell.change_state()
    if 'reset' in changed_id:
        points, fig = interactive_grid(25)
        grid = Grid(25)
        for point in points:
            cell = grid.__getitem__(point[0],point[1])
            cell.change_state()
    elif 'next' in changed_id:
        grid.update_grid()
        fig = create_grid(25, grid)
    return fig