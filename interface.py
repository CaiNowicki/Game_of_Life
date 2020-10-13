import plotly.graph_objects as go
from game_objects import Cell

cell= Cell()

def create_grid(n):
    x = [i + 0.5 for i in range(n)]
    y = [i + 0.5 for i in range(n)]
    fig = go.Figure(go.Scatter(x=x, y=y, marker = dict(size=25, symbol=1), line=dict(width=0)))
    #if n = 25, this fills whole square
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor = "black", tickvals = [x for x in range(n)],
                     range=[0,n],  scaleanchor="x", constrain="domain")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor = "black", tickvals = [x for x in range(n)],
                     range=[0,n], constrain="domain", scaleanchor="y")
    fig.update_layout(hovermode=False, clickmode="event")
#TODO
#adjust size of marker dynamically so it fills block regardless of n
#figure out how to capture mouseclicks on graph in Python

def update_cell(cell):
    #if detects a mouse click
    #determine which block contains mouse click
    #check if clickable == True
    #then call cell.change_state()
    pass

def clickable(grid):
    #if simulation has started
    #change cell.clickable to False for all cells in grid
    #if simulation has ended
    #change cell.clickable to True for all cells in grid
    pass
create_grid(5)