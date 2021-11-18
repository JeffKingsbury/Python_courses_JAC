# 1) Watch the video simple_game (in your exercises folder). Your task is to write a script that
# duplicates the game as shown in the video.
# For that you will use all the classes we created in class 07. All the class definitions are found
# in the file pythoncards.py (It is found in your exercises folder). Copy that file to your working
# directory.
# You will start your script by creating a new file and importing the classes as follows:
# import pythoncards as pc
# After importing the Python Cards Classes, you are ready to start. Good programming!

import pythoncards as pc


def titlebar():
    print("{:<20}".format('='*20))
    print("{}{:^18}{}".format("|", "Simple Card Game", "|"))
    print("{:<20}".format('='*20))
    print()


# Display title
titlebar()

# Create two players
player1 = input("Enter player 1: ")
player2 = input("Enter player 2: ")

print()

while True:
    # Build Deck
    deck = pc.SCardDeck()
    # Build hands
    hand1 = pc.SHand(player1)
    hand2 = pc.SHand(player2)
    # Deal 5 cards to each player
    for i in range(5):
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        # Display Player Hand and Value
        print("{:<15} {} :value: {}".format(
            hand1.owner, hand1, hand1.get_value()))
        print("{:<15} {} :value: {}".format(
            hand2.owner, hand2, hand2.get_value()))
        print()
        if hand1.get_value() > hand2.get_value():
            print("*** {} is the winner! ***".format(hand1.owner))
        elif hand1.get_value() < hand2.get_value():
            print("*** {} is the winner! ***".format(hand2.owner))
        else:
            print("*** It is a tie game! ***")
            print()

    choice = input('Would you like to play again (y or n): ')
    if choice != 'y':
        break
