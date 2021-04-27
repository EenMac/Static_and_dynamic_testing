import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()
        self.card1 = Card('diamonds', 1)
        self.card2 = Card('clubs', 2) 
        self.cards = [self.card1, self.card2]
    
    def test_check_for_ace(self):
        ace = self.game.check_for_ace(self.card1)
        self.assertEqual(True, ace)
    
    def test_for_no_ace(self):
        No_ace = self.game.check_for_ace(self.card2)
        self.assertEqual(False, No_ace)
    
    def test_highest_card(self):
        card1 = self.card1
        card2 = self.card2
        highest_card = self.game.highest_card(card1, card2)
        self.assertEqual(card2, highest_card)
    
    def test_cards_total(self):
        card1 = self.card1
        card2 = self.card2
        cardArray = [card1, card2]
        total = self.game.cards_total(cardArray)
        self.assertEqual("You have a total of 3", total)
    