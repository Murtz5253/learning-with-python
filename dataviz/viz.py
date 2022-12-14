#### For demo purposes

import numpy as np
import pandas as pd
import altair as alt

# set output to HTML
alt.renderers.enable("html")

# read in data
data = pd.read_csv("../data/data_student_1.csv")
# replace -1 values with NaN
data = data.replace(-1, np.nan)

# calculate mean score per question
data["score"] = data[["misc_1a", "misc_1b", "misc_1c", "misc_2a", "misc_2b",
                      "misc_3a", "misc_3b", "misc_3c", "misc_4a", "misc_4b",
                      "misc_5a", "misc_6a"]].mean(axis=1).round(1)

# scores chart
chart = alt.Chart(data).mark_point().encode(
    alt.X("question_id:N"),
    y="score:Q"
).properties(
    title="Student 1 Scores"
)
chart.configure_title(
    fontSize=20,
    font="Courier",
    anchor="start"
)
text = chart.mark_text(
    align="center",
    baseline="bottom",
    dx=0,
    dy=-5
).encode(
    text="score"
)
chart = chart + text

# time spent chart
chart1 = alt.Chart(data).mark_point().encode(
    alt.X("question_id:N"),
    y="time_spent_min:Q"
).properties(
    title="Student 1 Time Spent Data"
)
chart1.configure_title(
    fontSize=20,
    font="Courier",
    anchor="start"
)

# combine charts
chart = alt.vconcat(chart, chart1).configure_point(
    size=50,
    filled=True
)
# export chart
chart.save("test.html")
