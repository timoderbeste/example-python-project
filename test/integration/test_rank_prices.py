import unittest

from src.rank_prices import rank_prices


class TestRankPrices(unittest.TestCase):
    def test_rank_empty(self):
        prices = []
        result = rank_prices(prices)
        self.assertEqual(result, [])
        
    def test_rank_single(self):
        prices = [10]
        result = rank_prices(prices)
        self.assertEqual(result, [10])
    
    def test_rank_multiple(self):
        prices = [10, 100, 1]
        result = rank_prices(prices)
        self.assertEqual(result, [1, 10, 100])
