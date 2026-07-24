"""
Unit tests for the sentiment_analyzer function.

This module uses Python's unittest framework to validate the sentiment classification 
logic. It checks whether the sentiment_analyzer correctly identifies 
positive, negative, and neutral sentiments based on the provided input text.
"""

import unittest
from sentimentanalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    ''' A class that inherits the TestCase class of the unittest library. '''

    def test_sentiment_analyzer(self):
        ''' Analyze text sentiment via external API and return label and score '''

        # Test case for positive sentiment
        self.assertEqual(
            sentiment_analyzer('I love working with Python')['label'],
            'SENT_POSITIVE')

        # Test case for negative sentiment
        self.assertEqual(
            sentiment_analyzer('I hate working with Python')['label'],
            'SENT_NEGATIVE')

        # Test case for neutral sentiment
        self.assertEqual(
            sentiment_analyzer('I am neutral on Python')['label'],
            'SENT_NEUTRAL')

unittest.main()
