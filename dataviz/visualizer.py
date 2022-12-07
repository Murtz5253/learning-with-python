"""
Data visualization tool functions.
"""
# Import packages.
import numpy as np
import pandas as pd
import altair as alt

# Import functions.
from visualizerFunctions import *

# Initialize charts lists.
scoreCharts = []
timeCharts = []
# Initialize renderer.
alt.renderers.enable("html")

# Import student data.
data = importData("../data")

# For each student in dataset.
for i in range(0,len(data)):
    scoreCharts.append(createScoresChart(data[i]))
    timeCharts.append(createTimeSpentChart(data[i]))

# Combine charts.
chart = alt.vconcat(*scoreCharts, *timeCharts
# Format data points.
).configure_point(
    size=50,
    filled=True
)

# export chart
chart.save("test.html")
    
