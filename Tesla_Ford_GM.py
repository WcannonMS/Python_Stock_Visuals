# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:44:26 2020

@author: William Cannon
Note:  File001 Tesla, Ford and General Motors Stock Analysis
"""
#Import All Necessary Packages
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import column, row

#Read the Data File
TFGM = pd.read_csv('TSLA_F_GM.csv')

data = ColumnDataSource(TFGM)
TFGM['Date'] = pd.to_datetime(TFGM['Date'])
#plot1 Adjusted Closing Proces
plot1 = figure(x_axis_type = 'datetime', x_axis_label = 'Dates', y_axis_label = 'Adj. Close Price', title = '3 Stock Portfolio 10yr Adj. Close')
#plot1.line('datetime', 'Adj. Close Price', legend_label="some label")
plot1.line(x = TFGM['Date'], y = TFGM['GM_Adj Close'], color = 'red', legend_label='GM')
plot1.line(x = TFGM['Date'], y = TFGM['TSLA_Adj Close'], color = 'black', legend_label='TSLA')
plot1.line(x = TFGM['Date'], y = TFGM['F_Adj Close'], color = 'green', legend_label='F')
#plot1.line(x = TFGM['Date'], y = TFGM['S&P'], color = 'purple')
plot1.legend.location = "top_left"
output_file('PLOT001.html')
#plot2 high
plot2 = figure(x_axis_type = 'datetime', x_axis_label = 'Dates', y_axis_label = 'Volume', title = 'Volume')
plot2.line(x = TFGM['Date'], y = TFGM['GM_Volume'], color = 'red', legend_label='GM')
plot2.line(x = TFGM['Date'], y = TFGM['TSLA_Volume'], color = 'black', legend_label='TSLA')
plot2.line(x = TFGM['Date'], y = TFGM['F_Volume'], color = 'green', legend_label='F')
#plot2.line(x = TFGM['Date'], y = TFGM['S&P_RET'], color = 'purple')
plot2.legend.location = "top_left"
output_file('PLOT002.html')
#combined plots
row_layout = row(plot1, plot2)
output_file('twoplots.html')
show(row_layout)