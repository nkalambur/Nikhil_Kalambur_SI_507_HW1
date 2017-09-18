# Nikhil_Kalambur_SI_507_HW1

The 507F17_project1_cards.py contains code in Python that provides functionality to play basic card games. The main classes create Card and Deck object instances, allowing you to manipulate cards such as 2 of Spades and perform functionality against a standard 52 card deck, such as shuffling, re-sorting, and dealing hands. 

Specific functions exist as well. The Play War Game function mimics the card game "War" for 2 players. The Show Songs function fetches song data from iTunes based on user input search terms. Helper functions are also provided in another file to support these functions. 

The SI507F17_project1_tests.py file tests these pieces of code, and ultimately identified 3 root errors. First error relates to the rendering of face cards. Rather than returning "Ace of Diamonds", the Card() class returns "1 of Diamonds". (See test function: test_face_cards) The second error relates to the deal hand functionality. Ultimately, the deal hand function is not able to deal a hand of 52, nor does it seem to process the user input hand size properly. (See test functions: test_deal_hand2 and test_deal_hand3). Finally, the show song functionality does not work either. When searching for a specific song, the returned data is seemingly unrelated. (see test function: test_show_song). 


