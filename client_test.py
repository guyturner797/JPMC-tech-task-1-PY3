import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        print(getDataPoint(quote))
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  # Test to ensure ratio is determined as 1 for equally priced stocks
  def test_getRatio_Equal1(self):
      price_a = 110.0
      price_b = 110.0
      self.assertEqual(getRatio(price_a, price_b), 1)

  # Test to ensure ratio is > 1 when price a is greater than price b
  def test_getRatio_GreaterThan1(self):
      price_a = 110.0
      price_b = 90.0
      self.assertGreater(getRatio(price_a, price_b), 1)

  # Test to ensure ratio is < 1 when price a is less than price b
  def test_getRatio_LessThan1(self):
      price_a = 90.0
      price_b = 110.0
      self.assertLess(getRatio(price_a, price_b), 1)

  # Test to ensure when A price is 0 a ratio of 0 is returned
  def test_getRatio_AZero(self):
      price_a = 0.0
      price_b = 119.2
      self.assertEqual(getRatio(price_a, price_b), 0)

  # Test to ensure when B price is 0 a ZeroDivisionError is not raised
  def test_getRatio_BZero(self):
      self.assertIsNone(getRatio(119.2, 0))


if __name__ == '__main__':
    unittest.main()
