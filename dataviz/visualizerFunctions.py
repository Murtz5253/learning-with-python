"""
Data visualization tool functions.
"""
import numpy as np
import pandas as pd
import altair as alt
import glob

def importData(directory: str):
    """
    Function to import all csv data in directory.
    Args: directory: string - location of data
    Returns: data: list of DataFrame elements
    """
    # Define file list.
    fileList = glob.glob(directory+"/*.csv")
    # Sort by filename.
    fileList.sort()
    # Import and clean up all csv format data
    data = [pd.DataFrame(pd.read_csv(fileList[0])).replace(-1,np.nan)]
    for i in range(1,len(fileList)):
        data.append(pd.DataFrame(pd.read_csv(fileList[i])).replace(-1,np.nan))
    # Return dataset.
    return data

def createScoresChart(data: pd.DataFrame):
    """
    Function to create a chart to display one 
    student's mean scores vs. question ID.
    Args: data: Pandas DataFrame - data for one student
    Returns: chart: alt.Chart displaying the data
    """
    # calculate mean score per question
    data["score"] = data[["misc_1a","misc_1b","misc_1c","misc_2a","misc_2b",
                        "misc_3a","misc_3b","misc_3c","misc_4a","misc_4b",
                        "misc_5a","misc_6a"]].mean(axis=1).round(1)
    # Display data on chart.
    chart = alt.Chart(data).mark_point().encode(
        alt.X("question_id:N"),
        y="score:Q"
    # Add chart title.
    ).properties(
        title="Student " + str(round(data["student_id"].iat[0])) + " Mean Scores Data"
    )
    # Format chart title.
    chart.configure_title(
        fontSize=20,
        font="Courier",
        anchor="start"
    )
    # Add data value labels to data points.
    text = chart.mark_text(
        align="center",
        baseline="bottom",
        dx=0,
        dy=-5
    ).encode(
        text="score"
    )
    # Combine chart elements.
    chart = chart + text
    return chart

def createTimeSpentChart(data: pd.DataFrame):
    """
    Function to create a chart to display one 
    student's time spent vs. question ID.
    Args: data: Pandas DataFrame - data for one student
    Returns: chart: alt.Chart displaying the data
    """
    # Display data on chart.
    chart = alt.Chart(data).mark_point().encode(
        alt.X("question_id:N"),
        y="time_spent_min:Q"
    # Add chart title.
    ).properties(
        title="Student " + str(round(data["student_id"].iat[0])) + " Time Spent Data"
    )
    # Format chart title.
    chart.configure_title(
        fontSize=20,
        font="Courier",
        anchor="start"
    )
    return chart

def createTopicsChart(data: pd.DataFrame):
    """
    Function to create a chart to display one 
    student's mean score vs. topic/misconception.
    Args: data: Pandas DataFrame - data for one student
    Returns: chart: alt.Chart displaying the data
    """
    # Define all topics.
    topics = ["1a","1b","1c","2a","2b","3a",
              "3b","3c","4a","4b","5a","6a"]
    # Find mean score for each topic.
    scores = [data["misc_1a"].mean(),
              data["misc_1b"].mean(),
              data["misc_1c"].mean(),
              data["misc_2a"].mean(),
              data["misc_2b"].mean(),
              data["misc_3a"].mean(),
              data["misc_3b"].mean(),
              data["misc_3c"].mean(),
              data["misc_4a"].mean(),
              data["misc_4b"].mean(),
              data["misc_5a"].mean(),
              data["misc_6a"].mean(),]
    # Create new DataFrame for topics data.
    topicsData = pd.DataFrame({"topics":topics,"scores":scores})
    # Display data on chart.
    chart = alt.Chart(topicsData).mark_bar().encode(
        alt.X("scores:Q",scale=alt.Scale(domain=[0, 100], nice=False)),
        y="topics:N"
    # Add chart title.
    ).properties(
        title="Student " + str(round(data["student_id"].iat[0])) + " Topics Performance Data"
    )
    # Format chart title.
    chart.configure_title(
        fontSize=20,
        font="Courier",
        anchor="start"
    )
    return chart