"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 20: Python for Interactive Data Visualization on the Browser

Author: Jhesed Tacadena
Date: 2017-02-15

Section 9 Contents:
    128. Introduction to Bokeh
    129. The Bokeh Charts Interface
    130. The Boke Plotting Interface
    131. Customizing Plot Styles
    132. Coding Exercise 10: Plotting from Pandas Dataframes
    133. Solution 10
    134. Understanding the Structure behind the Graphs
    135. Time-series Plots
    136. More Visualization Examples with Bokeh
    137. Plotting Time Intervals of the Motion Detector
    138. Hover Tool Implementation
"""

# bokeh.models  # low level
# bokeh.plotting  # recommended
# bokeh.charts # use for now

from bokeh.charts import Scatter, output_file, show
from bokeh.plotting import figure #, output_file, show
import pandas

if __name__ == '__main__':

    # ----- (1) Test using bokeh.charts -----

    # Testing random data
    df = pandas.DataFrame(columns=['X', 'Y'])
    df['X'] = [1, 2, 3, 4, 5]
    df['Y'] = [6, 7, 8, 9, 10]
    p = Scatter(df, x='X', y='Y', title="Temperature Observation", 
        xlabel='Days of observations', ylabel='Temperature')

    output_file('Scatter_charts.html')  # Generate an HTML file
    # show(p)  # Show

    # ----- (2) Test using bokeh.plotting (recommended for more customization) -----
    
    # p = figure(plot_width=500, plot_height=400, title='Earthquake')
    p = figure(plot_width=500, plot_height=400)
    # help(p)
    p.title = 'Earthquake'
    p.title_text_color = 'Orange'
    p.title_text_font = 'Times'
    p.title_text_font_style = 'italic'
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_label = 'Times'
    p.yaxis.axis_label = 'Value'

    # p.circle(df['X'], df['Y'], size=10, color='red', alpha=0.5)
    # p.triangle(df['X'], df['Y'], size=10, color='red', alpha=0.5)
    p.triangle(df['X'], df['Y'], size=[5, 10, 15, 20, 25], color='red', alpha=0.5)
    output_file('Scatter_plotting.html')
    # show(p)

    # ----- (3) Exercise: Reading from excel -----

    df = pandas.read_excel("verlegenhuken.xlsx", sheetname=0)
    df["Temperature"] = df["Temperature"]/10
    df["Pressure"] = df["Pressure"]/10

    p = figure(plot_width=500, plot_height=400, tools='pan,resize', logo=None)

    p.title = "Temperature and Air Pressure"
    p.title_text_color = "Gray"
    p.title_text_font = "arial"
    p.title_text_font_style = "bold"
    p.xaxis.minor_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_label = "Temperature (°C)"
    p.yaxis.axis_label = "Pressure (hPa)"                  

    p.circle(df["Temperature"],df["Pressure"], size=0.5)
    output_file("Weather.html")
    show(p)

