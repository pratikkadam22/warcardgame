from io import StringIO
import unittest
from unittest import TestCase
from unittest.mock import patch
from war_main import generate_deck, play_war

class TestWar(TestCase):
    def test_deckgeneration(self):
        """Test the generation of the deck of cards"""
        deck = generate_deck()
        self.assertEqual(len(deck), 52, "Should be 52")

    def test_simplebattle(self):
        """Test a simple battle without a war"""
        deck = [{'A':14},{'K':13}]
        deck.extend([{3:3},{3:3}])
        with patch('sys.stdout', new = StringIO()) as output_text:
            play_war(deck)
            self.assertIn("A_cards wins!!!", output_text.getvalue())

    def test_startwar(self):
        """Test the results in case of a war"""
        deck = [{3:3}, {4:4}, {2:2}]
        deck.extend([{'A':14}, {'K':13}, {2:2}])
        with patch('sys.stdout', new = StringIO()) as output_text:
            play_war(deck)
            self.assertIn("IT'S A WAR", output_text.getvalue())
            self.assertIn("B_cards wins!!!", output_text.getvalue())
    
    def test_bothemptysets(self):
        """Test if both the list of cards are empty"""
        deck = []
        with patch('sys.stdout', new = StringIO()) as output_text:
            play_war(deck)
            self.assertIn("Both the set of cards are empty!", output_text.getvalue())

if __name__ == '__main__':
    unittest.main()