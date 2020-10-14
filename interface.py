import plotly.graph_objects as go

from game_objects import Cell, Grid


def create_grid(n, grid):
    x = [i for i in range(n)]
    y = [i for i in range(n)]
    traces = []
    for value_x in x:
        for value_y in y:
            cell = grid.__getitem__(value_x, value_y)
            trace = go.Scatter(x=[value_x + 0.5], y=[value_y + 0.5],
                               marker=dict(size=30, symbol=1, color="blue"), line=dict(width=0))
            traces.append(trace)
    fig = go.FigureWidget(data=traces)
    fig.update_layout(hovermode="closest", clickmode="event", plot_bgcolor="white", width=1000, height=1000, showlegend=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="black", tickvals=[x for x in range(n)],
                     range=[0, n], scaleanchor="x", constrain="domain")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="black", tickvals=[x for x in range(n)],
                     range=[0, n], constrain="domain", scaleanchor="y")
    scatter = fig.data[0]

    def update_cell(trace, points, selector):
        x = trace.x - 0.5
        y = trace.y - 0.5
        c = list(scatter.marker.color)
        cell = grid.__getitem__(x, y)
        cell.change_state()
        for i in points.points_inds:
            c[i] = "black"
            with fig.batch_update():
                scatter.marker.color = c


    scatter.on_click(update_cell)
    fig.show()


# TODO
# adjust size of marker dynamically so it fills block regardless of n
# figure out how to capture mouseclicks on graph in Python


def clickable(grid):
    # if simulation has started
    # change cell.clickable to False for all cells in grid by calling cell.change_click()
    # if simulation has ended
    # change cell.clickable to True for all cells in grid by calling cell.change_click()
    pass


grid = Grid(25)
create_grid(25, grid)
