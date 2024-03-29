"""
This file contains the tests to test proper working of views in django.
"""

from django.test import TestCase, Client
from django.urls import reverse
from topics.models import Problem


class TestViews(TestCase):
    """
    This class tests if the ecpected views are generated by checking status code and html template
    """

    def setUp(self):
        self.client = Client()

        # Need to add a test problem to datacase for view tests to work
        # This is because existing data is not loaded into the test DB
        test_problem = Problem()
        test_problem.problem_id = 1
        test_problem.topic_number = 1
        test_problem.save()

    def test_home_get(self):
        """ Testing view of home page"""
        response = self.client.get(reverse('topics-home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/home.html')

    def test_topic_get(self):
        """ Testing view of topics page"""
        response = self.client.get(reverse('topics-topic'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic.html')

    def test_problems_get(self):
        """ Testing view of problems page"""
        response = self.client.get(reverse('topics-problems'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/problems.html')

    def test_solutions_get(self):
        """ Testing view of solutions page"""
        response = self.client.get(reverse('topics-solutions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/solutions.html')

    def test_problem_detail_get(self):
        """ Testing view of problems detail page"""
        response = self.client.get(reverse('topics-problem-detail', kwargs={'problem_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/individual_problem.html')

    def test_solution_detail_get(self):
        """ Testing view of solutions detail page"""
        response = self.client.get(reverse('topics-solution-detail', kwargs={'problem_id': 1}))

        #self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/solutions_by_problem.html')


class TestTopicsViews(TestCase):
    """
    Created an extra class for topics subpages to avoid clutter.
    """

    def setUp(self):
        self.client = Client()

    def test_topic1_get(self):
        """ Testing view of topics sub page 1"""
        response = self.client.get(reverse('topics-topic1'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic1.html')

    def test_topic2_get(self):
        """ Testing view of topics sub page 2"""
        response = self.client.get(reverse('topics-topic2'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic2.html')

    def test_topic3_get(self):
        """ Testing view of topics sub page 3"""
        response = self.client.get(reverse('topics-topic3'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic3.html')

    def test_topic4_get(self):
        """ Testing view of topics sub page 4"""
        response = self.client.get(reverse('topics-topic4'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic4.html')

    def test_topic5_get(self):
        """ Testing view of topics sub page 5"""
        response = self.client.get(reverse('topics-topic5'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic5.html')

    def test_topic6_get(self):
        """ Testing view of topics sub page 6"""
        response = self.client.get(reverse('topics-topic6'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/topic6.html')
