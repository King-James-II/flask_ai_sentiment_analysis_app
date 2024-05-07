import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    """
    A test class to verify the functionality of the sentiment_analyzer function.
    """
    
    def test_sentiment_analyzer(self):
        """
        A test method to verify if sentiment_analyzer returns the correct sentiment label.
        """
        # Test positive sentiment
        test_res1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(test_res1["label"], "SENT_POSITIVE")

        # Test negative sentiment
        test_res2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(test_res2["label"], "SENT_NEGATIVE")

        # Test neutral sentiment
        test_res3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(test_res3["label"], "SENT_NEUTRAL")

if __name__ == '__main__':
    unittest.main()
