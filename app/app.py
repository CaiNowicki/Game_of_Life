import dash
import dash_bootstrap_components as dbc

meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]
external_stylesheets = [dbc.themes.SPACELAB]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = "Conway's Game of Life"
server = app.server
