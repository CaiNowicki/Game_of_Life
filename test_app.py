import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app_scripts.game_objects import Grid
import time
import plotly.graph_objects as go



meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]
external_stylesheets = [dbc.themes.SPACELAB]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = "Conway's Game of Life"
server = app.server

def create_grid(n, grid):
    fig = go.Figure()
    for x in range(n):
        for y in range(n):
            cell = grid.__getitem__(x, y)
            loc_x = [x + 0.5]
            loc_y = [y + 0.5]
            scatter = go.Scatter(x=loc_x, y=loc_y, marker=dict(size=30, symbol=1, color=cell.color), line=dict(width=0),
                                 mode='markers')
            fig.add_trace(scatter)

    fig.update_layout(hovermode=False, clickmode="event", plot_bgcolor="white", width=1000, height=1000,
                      showlegend=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="black", tickvals=[x for x in range(n)],
                     range=[0, n], scaleanchor="x", constrain="domain", showticklabels=False, ticks="")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="black", tickvals=[x for x in range(n)],
                     range=[0, n], constrain="domain", scaleanchor="y", showticklabels=False, ticks="")

    return fig

grid = Grid(25)
game = create_grid(25, grid)

app.layout = html.Div(
    html.Div([
        html.H1("John Conway's Game of Life"),
        html.Div("Written in Python using Plotly-Dash"),
        dcc.Graph(figure=game, id='live-update-game'),
        dcc.Interval(id='interval-component', interval=10, n_intervals=0),
        html.Div(grid.generation)
    ])
)

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
if __name__ == '__main__':
    app.run_server(debug=True)
