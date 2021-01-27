import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = pd.read_csv('C:/Users/user/Documents/SummerProject/ExtractedCairns/poles.csv')
print(df.tail())


fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="type"
                        , color = "type", zoom=3, height=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
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