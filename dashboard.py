import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import os

df = pd.read_csv('clean_data.csv', parse_dates=['timestamp_utc'])
cities = sorted(df['city_name'].unique())
pollutants = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']

app = dash.Dash(__name__)
app.title = "Dashboard Qualite de l'Air"

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

app.layout = html.Div([
    html.H1("Dashboard Qualite de l'Air", style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 20}),
    
    html.Div([
        html.Div([
            html.H6("Villes", style={'margin': 0, 'color': '#7f8c8d', 'fontSize': 12}),
            html.H2(id="villes", style={'color': '#1f77b4', 'margin': 0, 'fontSize': 24})
        ], style={'background': 'white', 'padding': '10px 20px', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'textAlign': 'center', 'minWidth': '100px', 'display': 'inline-block'}),
        html.Div([
            html.H6("Jours", style={'margin': 0, 'color': '#7f8c8d', 'fontSize': 12}),
            html.H2(id="jours", style={'color': '#1f77b4', 'margin': 0, 'fontSize': 24})
        ], style={'background': 'white', 'padding': '10px 20px', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'textAlign': 'center', 'minWidth': '100px', 'display': 'inline-block'}),
        html.Div([
            html.H6("Points", style={'margin': 0, 'color': '#7f8c8d', 'fontSize': 12}),
            html.H2(id="points", style={'color': '#1f77b4', 'margin': 0, 'fontSize': 24})
        ], style={'background': 'white', 'padding': '10px 20px', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'textAlign': 'center', 'minWidth': '100px', 'display': 'inline-block'}),
        html.Div([
            html.H6("AQI Moyen", style={'margin': 0, 'color': '#7f8c8d', 'fontSize': 12}),
            html.H2(id="aqi", style={'color': '#1f77b4', 'margin': 0, 'fontSize': 24})
        ], style={'background': 'white', 'padding': '10px 20px', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'textAlign': 'center', 'minWidth': '100px', 'display': 'inline-block'})
    ], style={'display': 'flex', 'gap': '10px', 'justifyContent': 'center', 'marginBottom': 15, 'flexWrap': 'wrap'}),
    
    html.Div([
        html.Div([
            html.Label("Ville:", style={'fontWeight': 'bold', 'fontSize': 13}),
            dcc.Dropdown(
                id='city-filter',
                options=[{'label': 'Toutes', 'value': 'Toutes'}] + [{'label': c, 'value': c} for c in cities],
                value='Toutes',
                style={'width': 180, 'display': 'inline-block'}
            )
        ], style={'display': 'inline-block', 'marginRight': 15}),
        
        html.Div([
            html.Label("Polluant:", style={'fontWeight': 'bold', 'fontSize': 13}),
            dcc.Dropdown(
                id='pollutant-filter',
                options=[{'label': 'Tous', 'value': 'Tous'}] + [{'label': p.upper(), 'value': p} for p in pollutants],
                value='Tous',
                style={'width': 140, 'display': 'inline-block'}
            )
        ], style={'display': 'inline-block', 'marginRight': 15}),
        
        html.Div([
            html.Label("Date:", style={'fontWeight': 'bold', 'fontSize': 13}),
            dcc.DatePickerRange(
                id='date-range',
                start_date=df['timestamp_utc'].min().date(),
                end_date=df['timestamp_utc'].max().date(),
                display_format='DD/MM/YYYY'
            )
        ], style={'display': 'inline-block', 'marginRight': 15})
    ], style={'textAlign': 'center', 'marginBottom': 15, 'padding': '15px', 'background': 'white', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)'}),
    
    html.Div([
        dcc.Graph(id='line', config={'displayModeBar': False})
    ], style={'background': 'white', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'padding': '10px', 'marginBottom': '15px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='box', config={'displayModeBar': False})
        ], style={'width': '48%', 'background': 'white', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'padding': '10px', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='heat', config={'displayModeBar': False})
        ], style={'width': '48%', 'background': 'white', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'padding': '10px', 'display': 'inline-block', 'float': 'right'})
    ], style={'marginBottom': '15px'}),
    
    html.Div([
        dcc.Graph(id='hour', config={'displayModeBar': False})
    ], style={'background': 'white', 'borderRadius': '10px', 'boxShadow': '0 2px 10px rgba(0,0,0,0.1)', 'padding': '10px'})
], style={'maxWidth': '1400px', 'margin': 'auto', 'padding': '20px', 'fontFamily': 'Arial', 'background': '#ecf0f1', 'minHeight': '100vh'})

@app.callback(
    [Output('line', 'figure'), Output('box', 'figure'), Output('heat', 'figure'),
     Output('hour', 'figure'), Output('villes', 'children'), Output('jours', 'children'),
     Output('points', 'children'), Output('aqi', 'children')],
    [Input('city-filter', 'value'), Input('pollutant-filter', 'value'),
     Input('date-range', 'start_date'), Input('date-range', 'end_date')]
)
def update(selected_city, selected_pollutant, start_date, end_date):
    df_f = df.copy()
    
    if selected_city != 'Toutes':
        df_f = df_f[df_f['city_name'] == selected_city]
    
    if start_date and end_date:
        start_date = pd.to_datetime(start_date).tz_localize(None)
        end_date = pd.to_datetime(end_date).tz_localize(None)
        df_f['timestamp'] = df_f['timestamp_utc'].dt.tz_localize(None)
        df_f = df_f[(df_f['timestamp'] >= start_date) & (df_f['timestamp'] <= end_date)]
    
    if df_f.empty:
        empty_fig = {'data': [], 'layout': {'title': 'Aucune donnee'}}
        return empty_fig, empty_fig, empty_fig, empty_fig, 0, 0, 0, "0.0"
    
    line = px.line(df_f, x='timestamp_utc', y='aqi', color='city_name', color_discrete_sequence=colors)
    line.update_layout(height=400, margin=dict(l=10, r=10, t=40, b=20), legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5), xaxis_title="Date", yaxis_title="AQI", plot_bgcolor='white', paper_bgcolor='white')
    line.update_xaxes(showgrid=True, gridcolor='#ecf0f1')
    line.update_yaxes(showgrid=True, gridcolor='#ecf0f1')
    
    box = px.box(df_f, x='city_name', y='aqi', color='city_name', color_discrete_sequence=colors)
    box.update_layout(height=400, margin=dict(l=10, r=10, t=40, b=20), showlegend=False, xaxis_title="Ville", yaxis_title="AQI", plot_bgcolor='white', paper_bgcolor='white')
    box.update_xaxes(showgrid=True, gridcolor='#ecf0f1')
    box.update_yaxes(showgrid=True, gridcolor='#ecf0f1')
    
    if selected_pollutant != 'Tous':
        corr = df_f[[selected_pollutant]].corr()
        heat = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r')
    else:
        heat = px.imshow(df_f[pollutants].corr(), text_auto=True, color_continuous_scale='RdBu_r')
    heat.update_layout(height=400, margin=dict(l=10, r=10, t=40, b=20), xaxis_title=None, yaxis_title=None, plot_bgcolor='white', paper_bgcolor='white')
    
    hour = px.bar(df_f.groupby(df_f['timestamp_utc'].dt.hour)['aqi'].mean().reset_index(), x='timestamp_utc', y='aqi', color_discrete_sequence=['steelblue'])
    hour.update_layout(height=400, margin=dict(l=10, r=10, t=40, b=20), xaxis_title="Heure", yaxis_title="AQI", plot_bgcolor='white', paper_bgcolor='white')
    hour.update_xaxes(showgrid=True, gridcolor='#ecf0f1')
    hour.update_yaxes(showgrid=True, gridcolor='#ecf0f1')
    
    return line, box, heat, hour, df_f['city_id'].nunique(), (df_f['timestamp_utc'].max() - df_f['timestamp_utc'].min()).days, len(df_f), f"{df_f['aqi'].mean():.1f}"

server = app.server

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run(debug=False, host='0.0.0.0', port=port)
