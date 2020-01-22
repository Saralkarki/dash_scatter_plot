import pandas as pd
import plotly.graph_objects as go

from map_box import mapbox_access_token

df = pd.read_csv('data/earthquake.csv')
df['text'] = df['Epicenter'] + ',' + df['Magnitude'].astype(str)
site_lat = df.Lat
site_lon = df.Long
locations_name = df.Epicenter

fig = go.Figure()


fig.add_trace(go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        text = df.text,
        marker=go.scattermapbox.Marker(
            size=9,
            color='rgb(242, 177, 172)',
            opacity=1
        ),
        hoverinfo= 'text'
    ))
annotations = [dict(
  
              # text I want to display. I used <br> to break it into two lines
              text = 'All the earthquakes in Nepal from 1994-June 2019', 
              
              # font and border characteristics
              font = dict(color = '#FFFFFF', size = 14), borderpad = 10, 
              
              # positional arguments
              x = 0.05, y = 0.05, xref = 'paper', yref = 'paper', align = 'left', 
              
              # don't show arrow and set background color
              showarrow = False, bgcolor = 'black'
              )]

# assigning the annotations to the layout
# df['annotations'] = annotations
fig.update_layout(
    title='Earthquake in Nepal',
     margin = dict(t = 50, b = 0, l = 0, r = 0),
    annotations = annotations,
    autosize = True ,
#     hovermode='x',
    showlegend= False,
    height = 800,
    paper_bgcolor = '#ffffff',
    
    mapbox=go.layout.Mapbox(
        
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
             lat = 28.75,
            lon = 84.85
        ),
        pitch=0,
        zoom=5.5,
        style='basic',
        
    ),
)

fig.show()