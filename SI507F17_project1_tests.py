# Do not change import statements.
import unittest
from SI507F17_project1_cards import *
import helper_functions

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained
# in the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
# If more than 3 tests fail, it should be because
# multiple of the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like,
# 	but you should try to make these tests
#   well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)


class Card_Tests(unittest.TestCase):
    # Test1: make sure the right suits are available
    def test_available_suits(self):
        c = Card()
        expected_suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        self.assertEqual(c.suit_names, expected_suits, "Test Suits")

    # Test2: make sure the right face cards are available
    def test_face_cards(self):
        fc = Card(0, 1)
        self.assertEqual(
            str(fc),
            "Ace of Diamonds",
            "Test face card translation")
        # This fails!

    # Test3: make sure the right number of cards/suit are available
    def test_rank_levels(self):
        rl = Card()
        expected_ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(rl.rank_levels, expected_ranks,
                         "Testing the provided rank levels")


class Deck_Tests(unittest.TestCase):
    # Testing the Deck class

    # Test that the first card in the deck is the Ace of Diamonds
    def test_unshuffled_first_card(self):
        d = Deck()
        first_card = str(d.cards[0])
        exp_first_card = "1 of Diamonds"
    # based on prior error, using 1 instead of Ace
        self.assertEqual(first_card, exp_first_card,
                         "Testing first card in deck is Ace of Diamonds")

    def test_unshuffled_second_card(self):
        d = Deck()
        first_card = str(d.cards[1])
        exp_first_card = "2 of Diamonds"
        self.assertEqual(first_card, exp_first_card,
                         "Testing second card in deck is 2 of Diamonds")

    def test_length_of_deck(self):
        d = Deck()
        l = len(d.cards)
        self.assertEqual(l, 52,
                         "Testing the size of the deck, should be 52")

    def test_pop_card(self):
        # loop over each card, pop it out, and make sure the deck is empty!
        d = Deck()
        for each_card in range(0, 52):
            d.pop_card()
        self.assertEqual(len(d.cards), 0,
                         "Testing after full deck pop," +
                         " there's no cards left in the deck")

    def test_shuffle(self):
        d = Deck()
        dd = Deck()
        d.shuffle()
        shuffled_list = [str(c) for c in d.cards]
        unshuffled_list = [str(c) for c in dd.cards]
        self.assertFalse(shuffled_list == unshuffled_list,
                         "Testing that shuffled decks - should be different")

    def test_sort(self):
        d = Deck()
        dd = Deck()
        d.shuffle()
        d.sort_cards()
        self.assertTrue(str(d) == str(dd),
                        "Testing that sorting the decks works")

    def test_replace_card(self):
        # This test checks that if after popping the
        # 1 of Diamonds and replacing it using the
        # replace_card function, that it gets added back to the list! Works
        d = Deck()
        dd = Deck()
        replace_this_card = d.cards[0]  # storing 1 of diamonds in str
        d.pop_card(0)  # popping this out
        self.assertFalse(str(d.cards[0]) == str(
            replace_this_card), "Should be false")

        # print(str(replace_this_card))
        # print(str(d.cards[0]))

        d.replace_card(replace_this_card)
        d.sort_cards()
        list_of_cards = [str(c) for c in d.cards]
        # print(str(d.cards[0]))
        self.assertTrue(str(replace_this_card) in list_of_cards, "True")
        self.assertTrue(str(d.cards[0]) == str(
            replace_this_card), "Should be true!")

    def test_replace_card2(self):
        # Test to see if adding an existing card to a deck adds multiple list
        # elements
        d = Deck()
        dd = Deck()

        try_this = d.cards[0]
        tt = str(try_this)
        dd.replace_card(try_this)
        l_of_cards = [str(c) for c in dd.cards]
        # print(l_of_cards.count(tt))
        self.assertEqual(
            l_of_cards.count(tt),
            1,
            "Testing that replace card didn't add existing element")

    def test_deal_hand(self):  # add assertEqual etc later
        d = Deck()

        my_hand = [str(c) for c in d.deal_hand(4)]

        self.assertEqual(
            len(my_hand),
            4,
            "Testing that full deck deals hand size of 4")

    def test_deal_hand2(self):
        d = Deck()
        print(len(d.cards))
        for each_card in range(0, 48):
            d.pop_card()

        print(len(d.cards))

        player1 = d.deal_hand(2)
        try:
            player2 = d.deal_hand(2)
            self.assertTrue(len(d.cards) == 0,
                            "Testing that after having 4 cards left that" +
                            "2 players can be dealth 2 hands of 2")
        except IndexError:
            assert False

    def test_deal_hand3(self):
        # Check if 1 person can receive a 52 card deck!
        d = Deck()

        deck_size = len(d.cards)

        try:
            hand = d.deal_hand(deck_size)
            list_of_cards_in_hand = [str(c) for c in hand]
            print(list_of_cards_in_hand)
        except IndexError:
            assert False
        # Fails


class War_Game_Tests(unittest.TestCase):
    # Testing the War Game function
    # Test that the play war game function returns a tuple
    def test_war(self):
        outcome = play_war_game(True)
        # print(outcome)
        self.assertEqual((type(outcome)), tuple)

    # Test that first element of tuple is in ['Player1', 'Player2', 'Tie']
    def test_war2(self):
        outcome = play_war_game(True)
        self.assertTrue(outcome[0] in ['Player1', 'Player2', 'Tie'])

    # Test that 2nd element is an integer
    def test_war3(self):
        outcome = play_war_game(True)
        self.assertEqual(type(outcome[1]), int)

    # Test that 3rd element is an integer
    def test_war4(self):
        outcome = play_war_game(True)
        self.assertEqual(type(outcome[2]), int)


class TestShowSong(unittest.TestCase):

    def test_show_song(self):
        s = show_song("David Bowie")
        self.assertEqual(s.artist, "David Bowie",
                         "Testing that search term is in the string method")
        # This Fails!


if __name__ == "__main__":
    unittest.main(verbosity=2)
