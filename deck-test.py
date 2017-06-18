#deck-test.py
import unittest
from deck import deck

"""
deck unit tests
"""
class TestDeckMethods(unittest.TestCase):
    def test_length(self):
        test1 = deck()
        self.assertEqual(len(test1.cards), 52)

    def test_deal_one_length(self):
        test2 = deck()
        test2.deal_one()
        self.assertEqual(len(test2.cards), 51)

    def test_deal_all_length(self):
        test3 = deck()
        test3.deal_all()
        self.assertEqual(len(test3.cards), 0)

    def test_deck_shuffle(self):
        test4 = deck()
        test4_copy = deck()
        test4.shuffle()
        self.assertEqual(len(test4.cards), 52)
        self.assertNotEqual(test4.cards, test4_copy.cards)

if __name__ == '__main__':
    unittest.main()
