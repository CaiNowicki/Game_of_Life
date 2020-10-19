import plotly.graph_objects as go
import sys
import plotly
import time

sys.path.append(r'C:\Users\caino\PycharmProjects\compsci\Game_of_Life')

from app_scripts.game_objects import Cell, Grid


def create_interactive_grid(n, grid):
    x = []
    y = []
    for i in range(n):
        for j in range(n):
            xvalue, yvalue = i, j
            x.append(xvalue + 0.5)
            y.append(yvalue + 0.5)

    fig = go.FigureWidget()
    scatter = go.Scatter(x=x, y=y, marker=dict(size=30, symbol=1, color="blue"), line=dict(width=0),
                         mode='markers')
    fig.add_trace(scatter)

    fig.update_layout(hovermode="closest", clickmode="event", plot_bgcolor="white", width=1000, height=1000,
                      showlegend=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="black", tickvals=[x for x in range(n)],
                     range=[0, n], scaleanchor="x", constrain="domain", showticklabels=False, ticks="")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="black", tickvals=[x for x in range(n)],
                     range=[0, n], constrain="domain", scaleanchor="y", showticklabels=False, ticks="")

    def update_cell(trace, points, selector):
        # take in click
        # find location in Grid
        # update cell state
        # change color of marker on visible graph
        for point in points.points_inds:
            x = point.x - 0.5
            y = point.y - 0.5
            cell = grid.__getitem__(x, y)
            cell.change_state()
        c = list(scatter.marker.color)
        for point in points.point_inds:
            c[point] = "black"
            with fig.batch_update():
                scatter.marker.color = c

    scatter.on_click(update_cell)
    return fig


# TODO
# adjust size of marker dynamically so it fills block regardless of n
# figure out how to capture mouseclicks on graph in Python and use those clicks to call update_cell
# this might be best completed with Dash


def clickable(grid):
    # if simulation has started
    # change cell.clickable to False for all cells in grid by calling cell.change_click()
    # if simulation has ended
    # change cell.clickable to True for all cells in grid by calling cell.change_click()
    pass


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
    grid.update_grid()
    return fig