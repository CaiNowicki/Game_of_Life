import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from pages import index

navbar = dbc.NavbarSimple(
    brand="John Conway's Game of Life",
    #brand_href='/',
    #children=[
    #    dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')),
    #    dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')),
    #    dbc.NavItem(dcc.Link('Visualizations', href='/visualizations', className='nav-link')),
    #],
    sticky='top',
    color='light',
    light=True,
    dark=False
)


footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Cai Nowicki, Lambda School Student', className='mr-2'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:cai.nowicki@gmail.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/dunkelweizen/Game_of_Life'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/cai-nowicki-82749312/'),
                ],
                className='lead'
            )
        )
    )
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    else:
        return dcc.Markdown('## Page Not Found')

if __name__ == '__main__':
    app.run_server(debug=True)

