import os

import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from data import df,df_1,df_2,df_3,df_4,df_5
import plotly.graph_objects as go
# from mapit import fig

from map_box import mapbox_access_token

annotations = [dict(
  
              # text I want to display. I used <br> to break it into two lines
              text = 'All the earthquakes in Nepal from 1994-June 2019', 
              
              # font and border characteristics
              font = dict(color = '#FFFFFF', size = 18), borderpad = 10, 
              
              # positional arguments
              x = 0.05, y = 0.05, xref = 'paper', yref = 'paper', align = 'left', 
              
              # don't show arrow and set background color
              showarrow = False, bgcolor = 'black'
              )]



# locations_name = df.Epicenter


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server



datamap = go.Data([go.Scattermapbox(
   
    lat = df.Lat,
    lon = df.Long,
    mode = 'markers',
    text = df.text,
    name = 'Eq is Nepal',
    
    marker=go.scattermapbox.Marker(
            size=9,
            color= ['red','green','yellow','blue','aqua'],
            opacity=0.5
        ),
        hoverinfo= 'text'
        )])

layoutmap = go.Layout(
    title='Earthquake in Nepal',
     margin = dict(t = 50, b = 0, l = 0, r = 0),
    annotations = annotations,
    autosize = True ,
    hovermode='y',
    showlegend= True,
    height = 500,
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
print(df.head())
fig = dict(data = datamap , layout = layoutmap)
# fig = dict (data =  [
#                 dict(
#                     lon = df_1['Long'],
#                     lat = df_1['Lat'],
#                     type = 'scattermapbox',
#                     name = 'ea',
#                     text = df_1.text,
#                     marker = dict(
#                         color = ['aqua','blue'],
#                         # showscale = True
#                     )
#                 ),
#                 dict(
#                      text = df_2.text,
#                     name = 'Earthquake',
#                     type = 'scattermapbox',
#                     lon = df_2['Long'],
#                     lat = df_2['Lat'],
#                     marker = dict(
#                         color = 'red',
#                         symbol = 'circle'
#                     )
#                 )
#             ], layout = layoutmap)

app.layout = html.Div([
    html.Div([
        html.H1('Maped Earthquakes in Nepal'),
        dcc.Graph(id='graph', figure = fig)   
        
    ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)