"""
This is a module for running multipe tests for visualizer functions.
The goal is to test four functions:
1. importing data function;
2. create score chart function;
3. create time spent chart function;
4. create topics chart function.
"""

import unittest
import altair as alt
import pandas as pd

from dataviz import visualizerFunctions

class TestViz(unittest.TestCase):
    """
    Unit test for data visualizer functions.
    """
    def test_import_smoke(self):
        """
        Smoke test for importData function:
        The test will exam whether the function will run when we call it.
        """
        directory = "."
        visualizerFunctions.importData(directory)

    def test_import_edge(self):
        """
        Edge test for importData function:
        The code will cause an exception if the directory is not a string variable.
        e.g., the input is an integer.
        """
        with self.assertRaises(TypeError):
            directory = 123456
            visualizerFunctions.importData(directory)

    def test_chart_smoke(self):
        """
        Smoke test for:
        (1) createScoresChart,
        (2) createTimeSpentChart,
        (3) createTopicsChart functions.
        """
        data = visualizerFunctions.importData("/Users/yilinchen/learning-with-python/tests")
        for i in range(0, len(data)):
            chart = alt.vconcat(visualizerFunctions.createScoresChart(data[i]),
                                visualizerFunctions.createTimeSpentChart(data[i]),
                                visualizerFunctions.createTopicsChart(data[i]))
            chart.save("student_" + str(round(data[i]["student_id"].iat[0])) + "_charts.html")

    def test_chart_edge1(self):
        """
        Edge test for three chart functions:
        The code will cause an exception if the input is not a pandas data frame.
        e.g., the input is a dictionary.
        """
        with self.assertRaises(AttributeError):
            data = visualizerFunctions.importData("/Users/yilinchen/learning-with-python/tests")
            data2 = pd.DataFrame.to_dict(data)
            for i in range(0, len(data2)):
                chart = alt.vconcat(visualizerFunctions.createScoresChart(data2[i]),
                                    visualizerFunctions.createTimeSpentChart(data2[i]),
                                    visualizerFunctions.createTopicsChart(data2[i]))
                chart.save("student_" + str(round(data2[i]["student_id"].iat[0])) + "_charts.html")

    def test_chart_edge2(self):
        """
        Edge test for three chart functions:
        The code will cause an exception if the input is not a pandas data frame.
        e.g., the input is a list.
        """
        with self.assertRaises(AttributeError):
            data = visualizerFunctions.importData("/Users/yilinchen/learning-with-python/tests")
            data2 = pd.values.tolist(data)
            for i in range(0, len(data2)):
                chart = alt.vconcat(visualizerFunctions.createScoresChart(data2[i]),
                                    visualizerFunctions.createTimeSpentChart(data2[i]),
                                    visualizerFunctions.createTopicsChart(data2[i]))
                chart.save("student_" + str(round(data2[i]["student_id"].iat[0])) + "_charts.html")
