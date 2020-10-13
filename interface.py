import plotly.graph_objects as go

def create_grid(n):
    x = [x for x in range(n)]
    y = [x for x in range(n)]
    fig = go.Figure(go.Scatter(x=[1.5], y=[1.5], marker = dict(size=25, symbol=1), line=dict(width=0)))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor = "black", tickvals = [x for x in range(n)],
                     range=[0,n],  scaleanchor="x", constrain="domain")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor = "black", tickvals = [x for x in range(n)],
                     range=[0,n], constrain="domain", scaleanchor="y")
    fig.show()

create_grid(5)