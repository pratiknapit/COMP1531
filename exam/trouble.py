'''
The backend for the double trouble game.
'''

# Put any global variables your implementation needs here

cards = []

def flip_card(card_obj):
    '''
    Takes in a card_obj which is a python dictionary consistsing of two keys:
     suit: Either "Hearts", "Spades", "Diamonds", or "Clubs"
     number: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K'

    E.G. {"suit": "Hearts", "number": "5"}

    This card is then added to the pile.

    If the card already exists in the pile, it will not be added.
    '''
    global cards

    card_valid = True
    for card in cards:
        if card_obj == card:
            card_valid = False

    if card_valid == True:
        cards.append(card_obj)

    return {}

def is_double_trouble():
    '''
    Returns true if the last two cards were the same number. False otherwise.
    If this function is called whilst true, the pile is reset to empty.
    '''
    
    global cards 

    if len(cards) < 2:
        return False

    if cards[-1]['number'] == cards[-2]['number']:
        clear()
        return True 
    
    return False

def is_trouble_double():
    '''
    Returns true if the last four cards had the same suit. False otherwise.
    If this function is called whilst true, the pile is reset to empty.
    '''
    global cards 

    if len(cards) < 4:
        return False
    
    if cards[-1]['suit'] == cards[-2]['suit'] == cards[-3]['suit'] == \
        cards[-4]['suit']:
        clear()
        return True
    
    return False

def is_empty():
    '''
    Returns a boolean that is true if the pile of cards is empty, false if it is not empty
    '''

    global cards

    if len(cards) == 0:
        return True 
    else:
        return False


def clear():
    '''
    Clears the pile and resets the game
    '''
    global cards

    cards = []

    return {} 