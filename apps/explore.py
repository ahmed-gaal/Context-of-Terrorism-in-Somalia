"""
Data exploration script
"""
import os
import cufflinks
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

# Load data into pandas DataFrame
df = pd.read_csv('notebooks/som.csv')

# Perform data manipulation
df['Month'] = pd.DatetimeIndex(df['Date']).month_name()
cols = ['Target Name', 'Weapon Name', 'Attack Name', 'Group Name']
num_cols = ['Property Value', 'Fatalities', 'Offender Fatalities',
            'Wounded']
state = df['State'].unique()
attack_type = df['Attack Name'].unique()
available_columns = df.columns
months = df['Month'].unique()
target_type = df['Target Name'].unique()
weapon_type = df['Weapon Name'].unique()
group_name = df['Group Name'].unique()
indics = df.loc[:, cols]
cardinal = df.loc[:, num_cols].astype('int64')

# Load in our mapbox token
px.set_mapbox_access_token(os.environ.get('TOKEN'))

# Set custom color scale
color_scale = ['#E22126', '#669278', '#16161A', '#C74D4F', '#161729',
               '#B42D52', '#9B5A9C', '#B4C756', '#A9595C', '#3AA484',
               '#3580A0', '#CE3A74', '#7EAFED', '#6192BA', '#2D2F89',
               '#465DAB', '#1E1F2E']

# Design layout of dashboard
layout = html.Div([
    html.Hr(),
    dbc.Row(
        dbc.Col(
            html.P('Consequences and Casualties of Terrorism in Somalia', style={
                'font-family': 'Overpass, sans-serif', 'font-weight': 'bold',
                'font-variant': 'small-caps', 'font-size': '200%'
            }), width={'size': 6, 'offset': 4}), className='row'),
    html.Hr(),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column1',
                        options=[{
                            'label': i, 'value': i
                        } for i in state],
                        value='Banaadir'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type1',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column1',
                        options=[{
                            'label': i, 'value': i
                        } for i in target_type],
                        value='Military'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type1',
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
                        id='xaxis-column2',
                        options=[{
                            'label': i, 'value': i
                        } for i in state],
                        value='Sanaag'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type2',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column2',
                        options=[{
                            'label': i, 'value': i
                        } for i in cardinal],
                        value='Fatalities'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type2',
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
    ]),
    html.Hr(),
    dbc.Row(
        dbc.Col(
            html.P('Distribution of Weapons and Attacks Employed by\
                Perpetrators',
            style={
                'font-family': 'Overpass, sans-serif', 'font-weight': 'bold',
                'font-variant': 'small-caps', 'font-size': '200%'
            }), width={'size': 6, 'offset': 4}), className='row'),
    html.Hr(),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column4',
                        options=[{
                            'label': i, 'value': i
                        } for i in weapon_type],
                        value='Melee'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type4',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
            dcc.Graph(
                id='gname-graph',
                responsive=True,
                config={
                    'displaylogo': False,
                    'showTips': True
                }
            )
            
            ], style={
                'font-variant': 'small-caps', 'font-weight': 'bold'
            }), width=6, sm=12, xs=12, md=6
        ),
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column5',
                        options=[{
                            'label': i, 'value': i
                        } for i in group_name],
                        value='Jabha East Africa'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type5',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
            dcc.Graph(
                id='pie-chart2',
                responsive=True,
                config={
                    'displaylogo': False,
                    'showTips': True
                }
            )
            ], style={
                'font-variant': 'small-caps', 'font-weight': 'bold'
            }), width=6, sm=12, xs=12, md=6
        )
    ], className='row'),
    html.Hr(),
    dbc.Row(
        dbc.Col(
            html.P('Precise Locations of Attacks on Topographical Depiction',
            style={
                'font-family': 'Overpass, sans-serif', 'font-weight': 'bold',
                'font-variant': 'small-caps', 'font-size': '200%'
            }), width={'size': 6, 'offset': 4}), className='row'),
    html.Hr(),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column3',
                        options=[{
                            'label': i, 'value': i
                        } for i in weapon_type],
                        value='Explosives'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type3',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column3',
                        options=[{
                            'label': i, 'value': i
                        } for i in state],
                        value='Banaadir'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type3',
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
                        'scrollZoom': True
                    }
                )
            ], style = {
                'font-variant': 'small-caps', 'font-weight': 'bold'
            }), width=12, xs=12, sm=12, md=12
        )
    ], className='row'),

])
@app.callback(
    Output('map-graph', 'figure'),
    Input('xaxis-column3', 'value'),
    Input('yaxis-column3', 'value'),
    Input('xaxis-type3', 'value')
)
def update_graph(xaxis_column, yaxis_column, xaxis_type):
    dff = df[df['State'] == yaxis_column]
    dff = dff[dff['Weapon Name'] == xaxis_column]
    fig = px.scatter_mapbox(dff, lat='latitude', lon='longitude',
                            color='Attack Name', size='Attack Type',
                            labels={'State': 'Attack Name'}, zoom=8,
                            mapbox_style='satellite-streets',
                            hover_data={
                                'latitude': False, 'longitude': False,
                                'Group Name': True, 'City': True,
                                'Attack Type': False, 'Target Name': True,
                                'Weapon Name': True
                            }, template='presentation',
                            color_discrete_sequence=color_scale)
    
    return fig
@app.callback(
    Output('bar-plot', 'figure'),
    Input('xaxis-column1', 'value'),
    Input('yaxis-column1', 'value'),
    Input('xaxis-type1', 'value')
)
def update_graph(xaxis_column, yaxis_column, xaxis_type):
    df1 = df[df['State'] == xaxis_column]
    df1 = df1[df1['Target Name'] == yaxis_column]
    fig = df1.iplot(
        asFigure=True, kind='bar', x='Group Name', y='Property Value',
        theme='white', subplots=True, yTitle='Total Amount in USD',
        subplot_titles=True, colorscale='Puor', xTitle='Groups',
        title='Value of Property Sabotaged', gridcolor='white'
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig
@app.callback(
    Output('pie-chart', 'figure'),
    Input('xaxis-column2', 'value'),
    Input('yaxis-column2', 'value'),
    Input('xaxis-type2', 'value'))
def update_graph_two(xaxis_column, yaxis_column, xaxis_type):
    dts = df[df['State'] == xaxis_column]
    fig = dts.iplot(
        asFigure=True, kind='pie', labels='Target Name', values=yaxis_column,
        hole=0.5, pull=0.02, textposition='inside', colors=color_scale,
        linecolor='black', theme='white', textinfo='percent', sort=False,
        title='Statistics of ' + str(yaxis_column) + ' in ' + str(xaxis_column)
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})
    
    return fig
@app.callback(
    Output('gname-graph', 'figure'),
    Input('xaxis-column4', 'value'),
    Input('xaxis-type4', 'value')
)
def gname_graph(xaxis_column, xaxis_type):
    df1 = df[df['Weapon Name'] == xaxis_column]
    fig = df1.iplot(
        asFigure=True, kind='bar', x="Group Name", y='Weapon Type',
        theme='white', gridcolor='white', colors=color_scale, yTitle='Group',
        xTitle='Instances Used', orientation='h', subplots=True,
        subplot_titles=True
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})
    return fig
@app.callback(
    Output('pie-chart2', 'figure'),
    Input('xaxis-column5', 'value'),
    Input('xaxis-type5', 'value')
)
def pie_chart(xaxis_column, xaxis_type):
    dff = df[df['Group Name'] == xaxis_column]
    dff1 = pd.DataFrame(
        dff['Attack Name'].value_counts(normalize=False)
    ).reset_index()
    fig = dff1.iplot(
        asFigure=True, kind='pie', labels='index', values='Attack Name',
        hole=0.5, pull=.02, textposition='inside', colorscale='piyg',
        theme='white', linecolor='black', textinfo='percent'
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 'r': 40, 't': 40})
    return fig