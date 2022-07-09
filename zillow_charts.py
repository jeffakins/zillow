# An app that displays the latest housing data from Zillow

# Imports

import pandas as pd

import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# Data Imports
home_prices = pd.read_csv('Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv') # Zillow Home Value Index 
inventory = pd.read_csv('Metro_invt_fs_uc_sfrcondo_sm_month.csv') # Home Inventory 
list_sale_price = pd.read_csv('Metro_mlp_uc_sfrcondo_sm_month.csv') # List and Sale Prices
price_cuts = pd.read_csv('Metro_sales_count_now_uc_sfrcondo_month.csv') # Sales Count and Price Cuts

# Graphs

fig = px.line(home_prices, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()