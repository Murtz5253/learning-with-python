"""
Data visualization tool functions.
"""
# Import packages.
import altair as alt

# Import functions.
from visualizerFunctions import *

# Initialize renderer.
alt.renderers.enable("html")

# Import student data.
data = importData("../data")

# Create, concatenate, and export charts
# for each student in dataset.
for i in range(0, len(data)):
    chart = alt.vconcat(createScoresChart(data[i]),
                        createTimeSpentChart(data[i]),
                        createTopicsChart(data[i]))
    chart.save("student_" + str(round(data[i]["student_id"].iat[0])) + "_charts.html")

# export chart
chart.save("test.html")
