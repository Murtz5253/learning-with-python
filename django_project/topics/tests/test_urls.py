"""
This file contains the tests to test proper working of urls in django.
"""

from django.test import SimpleTestCase

from django.urls import resolve, reverse
from topics.views import (
    home, topic, topic1, topic2, topic3, topic4, topic5, topic6, problems, problem_detail, solutions, solution_detail)


class TestUrls(SimpleTestCase):
    """
    This class takes in relative url and tests if correct absolute url is resloved.
    """

    def test_home_url_is_resolved(self):
        """ Resolving home page url"""
        url = reverse('topics-home')
        self.assertEqual(resolve(url).func, home)

    def test_topic_url_is_resolved(self):
        """ Resolving topics page url"""
        url = reverse('topics-topic')
        self.assertEqual(resolve(url).func, topic)

    def test_problems_url_is_resolved(self):
        """ Resolving problems page url"""
        url = reverse('topics-problems')
        self.assertEqual(resolve(url).func, problems)

    def test_solutions_url_is_resolved(self):
        """ Resolving solutions page url"""
        url = reverse('topics-solutions')
        self.assertEqual(resolve(url).func, solutions)

    def test_problem_detail_url_is_resolved(self):
        """ Resolving problem detail page url"""
        url = reverse('topics-problem-detail', kwargs={'problem_id': 1})
        self.assertEqual(resolve(url).func, problem_detail)

    def test_solution_detail_url_is_resolved(self):
        """ Resolving solution detail page url"""
        url = reverse('topics-solution-detail', kwargs={'problem_id': 1})
        self.assertEqual(resolve(url).func, solution_detail)


class TestTopicUrls(SimpleTestCase):
    """
    Created an extra class for topics subpages to avoid clutter.
    """

    def test_topic1_url_is_resolved(self):
        """ Resolving topics sub page 1 url"""
        url = reverse('topics-topic1')
        self.assertEqual(resolve(url).func, topic1)

    def test_topic2_url_is_resolved(self):
        """ Resolving topics sub page 2 url"""
        url = reverse('topics-topic2')
        self.assertEqual(resolve(url).func, topic2)

    def test_topic3_url_is_resolved(self):
        """ Resolving topics sub page 3 url"""
        url = reverse('topics-topic3')
        self.assertEqual(resolve(url).func, topic3)

    def test_topic4_url_is_resolved(self):
        """ Resolving topics sub page 4 url"""
        url = reverse('topics-topic4')
        self.assertEqual(resolve(url).func, topic4)

    def test_topic5_url_is_resolved(self):
        """ Resolving topics sub page 5 url"""
        url = reverse('topics-topic5')
        self.assertEqual(resolve(url).func, topic5)

    def test_topic6_url_is_resolved(self):
        """ Resolving topics sub page 6 url"""
        url = reverse('topics-topic6')
        self.assertEqual(resolve(url).func, topic6)