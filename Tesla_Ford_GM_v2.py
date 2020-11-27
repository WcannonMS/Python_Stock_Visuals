# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 02:30:04 2020
@author: William Cannon
Note:  File001 Tesla, Ford and General Motors Stock Analysis
Updates
-Hovertool
-Updated source .csv to match extracts.  Changed column formatting ot match.
"""

import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d #Added 10/25/20 to support labels
from bokeh.models.annotations import Label, LabelSet #Added 10/25/20 to support labels
from bokeh.models import CategoricalColorMapper #Added 11/18/20 to support hover tooltip
from bokeh.models import HoverTool #Added 11/18/20 to support hover tooltip

#Import the Data & Read the data file into a dataframe
TFGM = pd.read_csv('TSLA_F_GM_v2.csv')
TFGM['Date'] = pd.to_datetime(TFGM['Date'])
#Create dataframes for each stock
GMdf = TFGM.loc[TFGM["Name"] == "GM"]
Fdf =  TFGM.loc[TFGM["Name"] == "F"]
TSLAdf = TFGM.loc[TFGM["Name"] == "TSLA"]
#Create hoverTool
hover_tool = HoverTool(
    tooltips = [
    ('Date', '@Date{%F}'),
    ('Ticker Symbol', '@Name'),
    ('High Price', '$@High{0.00 a}'),
    ('Low Price', '$@Low{0.00 a}'),
    ('Adj Close', '$@{Adj Close}{%0.2f}')
    ],

    formatters = {
        '@Date'        : 'datetime', # use 'datetime' formatter for '@date' field
        '@{Adj Close}' : 'printf',   # use 'printf' formatter for '@{adj close}' field
                                      # use default 'numeral' formatter for other fields
    },
    #mode='vline' # display a tooltip whenever the cursor is vertically in line with a glyph
)

#Split the data into separate ColumnDataSource() objects using the dataframes
GMdata= ColumnDataSource(TFGM.loc[TFGM["Name"] == "GM"]) #Column data source for GM, filters data down into smaller data sets
Forddata = ColumnDataSource(TFGM.loc[TFGM["Name"] == "F"]) #Column data source for Ford, filters data down into smaller data sets
Tesladata = ColumnDataSource(TFGM.loc[TFGM["Name"] == "TSLA"]) #Column data source for Tesla, filters data down into smaller data sets

#plot1 Adjusted Closing Proces 
plot1 = figure(x_axis_type = 'datetime', x_axis_label = 'Dates', y_axis_label = 'Adj. Close Price', title = '3 Stock Portfolio 10yr Adj. Close', tools = [hover_tool])
plot1.line(x = 'Date', y = 'Adj Close', color = 'red', legend_label='GM', source = GMdata) #row for GM
plot1.line(x = 'Date', y = 'Adj Close', color = 'black', legend_label='TSLA', source = Tesladata) #row for Tesla
plot1.line(x = 'Date', y = 'Adj Close', color = 'green', legend_label='F', source = Forddata) # row for Ford
plot1.legend.location = "top_left"
output_file('PLOT001.html')



#Create hoverTool for plot 2
hover_tool = HoverTool(
    tooltips = [
        ('Date', '@Date{%F}'),
        ('Ticker Symbol', '@Name'),
        #('Volume', '@Volume{0,0.000}'),
        ('Volume', '@Volume{(0.00 a)}'),
        #('Low Price', '@Low'),
      ('Adj Close', '$@{Adj Close}{%0.2f}')
    ],

    formatters = {
        '@Date'        : 'datetime', # use 'datetime' formatter for '@date' field
        '@{Adj Close}' : 'printf',   # use 'printf' formatter for '@{adj close}' field
                                      # use default 'numeral' formatter for other fields
    },
    #mode='vline' # display a tooltip whenever the cursor is vertically in line with a glyph
)

#plot2 high
#plot2 = figure(x_axis_type = 'datetime', x_axis_label = 'Dates', y_axis_label = 'Volume', title = 'Volume', tooltips = TOOLTIPS)
plot2 = figure(x_axis_type = 'datetime', x_axis_label = 'Dates', y_axis_label = 'Volume', title = 'Volume', tools = [hover_tool])
plot2.line(x = 'Date', y = 'Volume', color = 'red', legend_label='GM', source = GMdata)
plot2.line(x = 'Date', y = 'Volume', color = 'black', legend_label='TSLA', source = Tesladata)
plot2.line(x = 'Date', y = 'Volume', color = 'green', legend_label='F', source = Forddata)
plot2.legend.location = "top_right"
output_file('PLOT002.html')
#combined plots
row_layout = row(plot1, plot2)
output_file('twoplots.html')
show(row_layout)
