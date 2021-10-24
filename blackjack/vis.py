"""
Variety of ways to nicely dislay card representations
Width of terminal may impact vpython
"""


def print_cards(cardlist):
    for card in zip(*cardlist):
            print('   '.join(card))

def print_card(*cards):
    for line in zip(*cards):
        print('   '.join(line))


def reg_card_vpython(card):
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    vpython = [

         '  ╔════════════╗',
        f'  ║ {v:<5}      ║',
         '  ║            ║',
         '  ║            ║',
        f'  ║     {s:^3}    ║',
         '  ║            ║',
         '  ║            ║',
         '  ║            ║',
        f'  ║      {v:>5} ║',
         '  ╚════════════╝'
    ]

    return vpython


def mini_card_vpython(card):
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    vpython = [
         '╔══════╗',
        f'║ {v:<3}  ║',
        f'║      ║',
        f'║  {s:>3} ║',
         '╚══════╝'
         ]

    return vpython


def tiny_card_vpython(card):
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    vpython = [
         '╔════╗',
        f'║ {v:<2} ║',
        f'║ {s:>2} ║',
         '╚════╝'     ]

    return vpython


def large_card_vpython(card):
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    vpython = [

         '   ┌─────────────────┐',
        f'   │ {v:<5}           │',
         '   │                 │',
         '   │                 │',
         '   │                 │',
         '   │                 │',
        f'   │        {s}        │',
         '   │                 │',
         '   │                 │',
         '   │                 │',
         '   │                 │',
         '   │                 │',
        f'   │           {v:>5} │',
         '   └─────────────────┘'

    ]

    return vpython


reg_hidden_card = [
     '   ╔════════════╗',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ╚════════════╝'
     ]


v, s = 'V', 'S'

card_vpythons = {

'small_card_vis' : [
     '╔══════╗',
    f'║ {v:<3}  ║',
    f'║ {s:>3}  ║',
    f'║      ║',
     '╚══════╝'
     ],


'mini_card_vis' : [
     '╔══════╗',
    f'║ {v:<3}  ║',
    f'║      ║',
    f'║  {s:>3} ║',
     '╚══════╝'
     ],


'thick_border_vis' : [

     '  ╔════════════╗',
    f'  ║ {v:<5}      ║',
     '  ║            ║',
     '  ║            ║',
    f'  ║     {s:^3}    ║',
     '  ║            ║',
     '  ║            ║',
     '  ║            ║',
    f'  ║      {v:>5} ║',
     '  ╚════════════╝'
     ],


'thin_border_vis' : [

    f'   ┌───────────┐',
    f'   │ {v:<5}     │',
     '   │           │',
     '   │           │',
     '   │           │',
    f'   │     {s}     │',
     '   │           │',
     '   │           │',
     '   │           │',
    f'   │     {v:>5} │',
     '   └───────────┘'
     ]

}

# print_card(card_vpythons['thick_border_vis'])


hidden_cards = {


'mini_thick_hidden_card' : [
     '╔══════╗',
     '║░░░░░░║',
     '║░░░░░░║',
     '║░░░░░░║',
     '╚══════╝'
     ],


'reg_thick_hidden_card' : [
     '   ╔════════════╗',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ║░░░░░░░░░░░░║',
     '   ╚════════════╝'
     ],


'small_thin_hidden_card' : [

     '┌────────┐',
     '│░░░░░░░░│',
     '│░░░░░░░░│',
     '│░░░░░░░░│',
     '│░░░░░░░░│',
     '│░░░░░░░░│',
     '└────────┘'
     ],

'reg_thin_hidden_card' : [
     '   ┌───────────┐',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   │░░░░░░░░░░░│',
     '   └───────────┘'
     ],

'large_thin_hidden_card' : [
 '   ┌─────────────────┐',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   │░░░░░░░░░░░░░░░░░│',
 '   └─────────────────┘'
]

}

# print_card(hidden_cards['reg_thick_hidden_card'])
