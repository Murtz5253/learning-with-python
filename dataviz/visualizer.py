"""
Data visualization tool functions.
"""
# Import packages.
import altair as alt

# Import functions.
import visualizerFunctions as vf 

# Initialize renderer.
alt.renderers.enable("html")

# Import student data.
data = vf.importData("../data")

# Create, concatenate, and export charts
# for each student in dataset.
for i in range(0, len(data)):
    chart = alt.vconcat(vf.createScoresChart(data[i]),
                        vf.createTimeSpentChart(data[i]),
                        vf.createTopicsChart(data[i]))
    chart.save("student_" + str(round(data[i]["student_id"].iat[0])) + "_charts.html")

# export chart
chart.save("test.html")
