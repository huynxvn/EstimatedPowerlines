import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html



df = pd.read_csv('C:/Users/user/Documents/SummerProject/ExtractedCairns/poles.csv')
print(df.tail())


fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="type"
                        , color = "type", zoom=3, height=500)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
app.run_server(debug=True)
'''
fig = go.Figure(data=go.Scattergeo(
        lon = df['lon'],
        lat = df['lat'],
        text = df['score'],
        mode = 'markers',
        marker_color = df['score'],
        ))

fig.show()
'''