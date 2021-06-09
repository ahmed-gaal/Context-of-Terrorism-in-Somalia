"""
Data exploration script
"""
import os
from typing import Container
import cufflinks
import pandas as pd
import notebooks.utils as ut
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app


df = pd.read_csv('notebooks/som.csv')
df['Month'] = pd.DatetimeIndex(df['Date']).month_name()

cols = ['Target Name', 'Weapon Name', 'Attack Name']
num_cols = ['Property Value', 'Fatalities', 'Offender Fatalities',
            'Wounded']
state = df['State'].unique()
attack_type = df['Attack Name'].unique()
available_columns = df.columns
months = df['Month'].unique()
target_type = df['Target Name'].unique()
weapon_type = df['Weapon Name'].unique()
indics = df.loc[:, cols]
cardinal = df.loc[:, num_cols]

px.set_mapbox_access_token(os.environ.get('TOKEN'))


def slice_df(df, element, item):
    df = df[df[element] == item]
    return df

#fig = px.scatter_mapbox(, lat='latitude', lon='longitude',
#                  color='weapon_name', size='weapon_type',
#                  labels={'state': 'attack_name'}, zoom=4, mapbox_style='dark')


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='xaxis-column2',
                            options=[{
                                'label': i, 'value': i
                            } for i in state],
                            value='Banaadir'
                        ),
                        dcc.RadioItems(
                            id='xaxis-type2',
                            labelStyle={'display': 'inline-block'}
                        )
                    ], style={
                        'width': '48%', 'display': 'inline-block',
                        'color': 'black'
                    }),

                    dcc.Graph(
                        id='bar-plot',
                        responsive=True,
                        config={
                            'displaylogo': False,
                            'showTips': True
                        }
                    )
                ], style = {
                    'font-variant': 'small-caps', 'font-weight': 'bold'
                }), width=6, xs=12, sm=12, md=6
            ),
            dbc.Col(
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='xaxis-column3',
                            options=[{
                                'label': i, 'value': i
                            } for i in state],
                            value='Banaadir'
                        ),
                        dcc.RadioItems(
                            id='xaxis-type3',
                            labelStyle={'display': 'inline-block'}
                        )
                    ], style={
                        'width': '48%', 'display': 'inline-block',
                        'color': 'black'
                    }),
                dcc.Graph(
                    id='pie-chart',
                    responsive=True,
                    config={
                        'showTips': True,
                        'displaylogo': False
                    }
                )
                ], style = {
                    'font-variant': 'small-caps', 'font-weight': 'bold'
                }), width=6, xs=12, sm=12, md=6
            )
        ])
    ]),
    html.Hr(),
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='xaxis-column',
                            options=[{
                                'label': i, 'value': i
                            } for i in attack_type],
                            value='Assassination'
                        ),
                        dcc.RadioItems(
                            id='xaxis-type',
                            labelStyle={'display': 'inline-block'}
                        )
                    ], style={
                        'width': '48%', 'display': 'inline-block',
                        'color': 'black'
                    }),
                    html.Div([
                        dcc.Dropdown(
                            id='yaxis-column',
                            options=[{
                                'label': i, 'value': i
                            } for i in state],
                            value='Banaadir'
                        ),
                        dcc.RadioItems(
                            id='yaxis-type',
                            labelStyle={'display': 'inline-block'}
                        )
                    ], style={
                        'width': '48%', 'display': 'inline-block',
                        'color': 'black'
                    }),

                    dcc.Graph(
                        id='map-graph',
                        responsive=True,
                        config={
                            'displaylogo': False,
                            'showTips': True,
                            'scrollZoom': False
                        }
                    )
                ], style = {
                    'font-variant': 'small-caps', 'font-weight': 'bold'
                }), width=12, xs=12, sm=12, md=12
            )
    ], className='row'),

    ])
])

@app.callback(
    Output('map-graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value')
)
def update_graph(xaxis_column, yaxis_column, xaxis_type):
    dff = df[df['State'] == yaxis_column]
    fig = px.scatter_mapbox(dff, lat='latitude', lon='longitude',
                            color='Weapon Name', size='Weapon Type',
                            labels={'State': 'Attack Name'}, zoom=4,
                            mapbox_style='dark')
    
    return fig


@app.callback(
    Output('bar-plot', 'figure'),
    Input('xaxis-column2', 'value'),
    Input('xaxis-type2', 'value')
)
def update_graph(xaxis_column, xaxis_type):
    df1 = df[df['State'] == xaxis_column]
    fig = df1.iplot(
        asFigure=True, kind='scatter', mode='lines', x='Date',
        y=['Target Name', 'Attack Name', 'Weapon Name'],
        theme='polar', interpolation='spline'
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig


@app.callback(
    Output('pie-chart', 'figure'),
    Input('xaxis-column3', 'value'),
    Input('xaxis-type3', 'value'))
def update_graph_two(xaxis_column, xaxis_type):
    dts = df[df['State'] == xaxis_column]
    colors = ['#7EAFED', '#6192BA', '#2D2F89', '#465DAB', '#1E1F2E']
    fig = dts.iplot(
        asFigure=True, kind='pie', labels='Target Name', values='Property Value',
        hole=0.5, pull=0.02, textposition='inside', colors=colors,
        linecolor='black', theme='white', textinfo='percent', sort=False
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})
    
    return fig
#def update_graph(xaxis_column, yaxis_column, xaxis_type):
#    dff = df[df['state'] == yaxis_column]
#    clr = ['#54408c']
#    fig = px.scatter_mapbox(dff, lat='latitude', lon='longitude',
#                  color='weapon_name', size='attack_type',
#                  labels={'state': 'attack_name'}, zoom=4, mapbox_style='dark')
    #fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

#   return fig