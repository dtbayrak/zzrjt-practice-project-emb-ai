import unittest
from sentimentanalysis.sentiment_analysis import sentiment_analyzer

#A class that inherits the TestCase class of the unittest library.
class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
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