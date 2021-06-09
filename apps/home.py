"""
Home page script
"""
import dash_html_components as html 
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1('Introduction', style={
                'font-family': 'Overpass, sans-serif',
                'font-size': '450%', 'font-weight': 'bold',
                'font-variant': 'small-caps'
            },className='text-center'), className='mb-5 mt-5',
            width=12, xs=6, sm=6, md=6)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dbc.Container([
                    html.P(children='Somalia is a coastal country that lies\
                                at the Horn of Africa from the Gulf of Aden\
                                to the Indian Ocean. It has a coastline of\
                                more than 3, 300 km making Somalia the\
                                country with the longest coastline in\
                                Mainland Africa.'),
                    html.Hr(),
                    html.P(children='Somalia was ravaged with war which went\
                                on for almost the past 3 decades after the\
                                toppling of the military regime governed by\
                                Major Gen. Mohamed Siad Barre. This gave\
                                birth to Somalia’s Civil War and clan\
                                factions began fighting for power.'),
                    html.P(children='Many civilians were annihilated and many\
                                more fled the country as refugees in\
                                neighbouring Kenya and all over the world.')
                    ], style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%',
                        'font-weight': 'normal'
                    }))
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dbc.Container([
                    html.P(children='Terrorism is defined as the threatened\
                                or actual use of illegal force and violence\
                                by a non-state actor to attain a political,\
                                economic, religious or social goal through\
                                fear, coercion, or intimidation.',
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    }),
                    html.P(children='Somalia has faced quite a strife for\
                                almost 30 years and most of those was between\
                                clans. Up to date, clans engage in armed\
                                conflict attributed to diverse motives that\
                                are not terrorism.',
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    }),
                    html.P(children='This dashboard will reveal insights on\
                                the types of attacks prevalent in Somalia,\
                                Where these attacks are mostly targeted and\
                                what types of weapons are employed. This will\
                                provide a clear understanding of context of\
                                terrorism in Somalia.',
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    })
                ])
            )
        ]),
        html.Hr()
    ])
])
