from random import randint

class Player(object):

    # Classe pour le joueur

    def __init__(self, bankroll=1000, hand=['', '', ''], sum=0):
        self.bankroll = bankroll
        self.hand = hand
        self.sum = sum

    def add_money(self, amount):
        self.bankroll += amount

    def remove_money(self, amount):
        self.bankroll -= amount


class Dealer(object):

    def __init__(self, hand=['', '', ''], sum=0):
        self.hand = hand
        self.sum = sum


class Deck(object):

    #  Classe pour du croupier

    def __init__(self, paquet):
        paquet = []
        for suite in ['coeur', 'pique', 'carreau', 'trefle']:
            for carte in range(2, 15):
                carte_nb = carte
                if carte_nb == 11:
                    carte_nb = 'V'
                    carte = 10
                elif carte_nb == 12:
                    carte_nb = 'D'
                    carte = 10
                elif carte_nb == 13:
                    carte_nb = 'R'
                    carte = 10
                elif carte_nb == 14:
                    carte_nb = 'As'
                    carte = 11
                paquet.append({'suite': suite, 'carte': carte_nb, 'valeur': carte})
        self.jeu = paquet


def print_board():
    print 'votre main est : ', sam.hand[0]['carte'],\
        sam.hand[0]['suite'], 'et', sam.hand[1]['carte'],\
        sam.hand[1]['suite'],
    print('\n')
    print 'la main du dealer est : ', dealer.hand[0]['carte'],\
        dealer.hand[0]['suite']


def print_sum():
    print 'vous avez :', sam.sum
    print 'le dealer a :', dealer.sum


def init_game(player, dealer):
    choix = randint(0, 54)
    sam.hand[0] = deck.jeu[choix]
    choix = randint(0, 54)
    dealer.hand[0] = deck.jeu[choix]
    choix = randint(0, 54)
    sam.hand[1] = deck.jeu[choix]
    choix = randint(0, 54)
    dealer.hand[1] = deck.jeu[choix]


def stand_or_hit():
    value = ''
    while value.lower() not in ['yes', 'no', 'y', 'n']:
        value = raw_input('Voulez vous une nouvelle carte ? [Y/N]')
        print('\n')
    if value.lower() in ['yes', 'y']:
        answer = True
        return answer
    else:
        answer = False
        return answer


def test_win(player, dealer):
    if dealer.sum == sam.sum == 21:
        condition = 1
        return condition
    elif dealer <= sam.sum:
        condition = 2
        return condition
    elif dealer >= sam.sum:
        condition = 3
        return condition


def update_sum(player, dealer):
    player.sum = player.hand[0]['valeur'] + player.hand[1]['valeur']
    dealer.sum = dealer.hand[0]['valeur']


if __name__ == '__main__':
    sam = None
    dealer = None
    jeu = list()
    sam = Player(1000)
    dealer = Dealer()
    deck = Deck(jeu)
    value = ''
    while value.lower() not in ['yes', 'no', 'y', 'n']:
        value = raw_input("Voulez vous jouer aux Morpions? [Y/N] ")
    play_game = True if value.lower() in ['yes', 'y'] else False
    while play_game:

        print('\n')
        print('Vous avez :'), sam.bankroll, 'Euros'
        print '\n'
        mise = int(raw_input('Combien voulez vous miser ? '))
        print '\n'
        sam.remove_money(mise)
        print('Vous avez :'), sam.bankroll, 'Euros \n'
        print('Le dealer distribu \n')
        init_game(sam, dealer)
        update_sum(sam, dealer)
        print_board()
        print '\n'
        print_sum()
        print '\n'
        selection = stand_or_hit()

        if selection:

            print('Le dealer vous donne une carte')
            choix = randint(0, 54)
            sam.hand[2] = deck.jeu[choix]
            sam.sum += int(sam.hand[2]['valeur'])
            print('Vous tirez un :'), sam.hand[2]['carte'],\
                sam.hand[2]['suite']
            print '\n'
            print_sum()
            print '\n'

            if sam.sum >= 21:
                print ('Vous avez perdu !')

            else:

                print ('Le dealer tourne ca carte et il a un :'),\
                    dealer.hand[1]['carte'], dealer.hand[1]['suite']
                dealer.sum += int(dealer.hand[1]['valeur'])
                print ('le dealer a '), dealer.sum

                condition = test_win(sam, dealer)
                if condition == 2:
                    choix = randint(0, 54)
                    dealer.hand[2] = deck.jeu[choix]
                    print ('Le dealer tire une carte : '),\
                        dealer.hand[2]['carte'], dealer.hand[2]['suite']
                    dealer.sum += int(dealer.hand[2]['valeur'])
                    print('\n')
                    print ('Le dealer a :'), dealer.sum
                    print('\n')

                    test_win(sam, dealer)
                    if condition:
                        print('Vous remportez la manche')
                        sam.add_money(mise*2)

                    elif condition == 3:
                        print 'le dealer remport la manche'

                    elif condition == 1:
                        print 'egalite'
                        sam.add_money(mise)

                elif condition == 3:
                    print 'le dealer remport la manche'

                elif condition == 1:
                    print 'egalite'
                    sam.add_money(mise)
        else:
            # Vous gadez votre main
            print('Vous gardez :'), sam.sum
            print('\n')
            print ('Le dealer tourne sa carte et il a un :'),\
                dealer.hand[1]['carte'], dealer.hand[1]['suite']
            dealer.sum += int(dealer.hand[1]['valeur'])
            print ('le dealer a '), dealer.sum

            condition = test_win(sam, dealer)
            if condition == 2:
                choix = randint(0, 54)
                dealer.hand[2] = deck.jeu[choix]
                print ('Le dealer tire une carte : '),\
                    dealer.hand[2]['carte'], dealer.hand[2]['suite']
                dealer.sum += int(dealer.hand[2]['valeur'])
                print('\n')
                print ('Le dealer a :'), dealer.sum
                print('\n')

                test_win(sam, dealer)
                if condition == 2:
                    print('Vous remportez la manche')
                    print('\n')
                    sam.add_money(mise*2)

                elif condition == 3:
                    print 'le dealer remport la manche'
                    print('\n')

                elif condition == 1:
                    print 'egalite'
                    sam.add_money(mise)

            elif condition == 2:
                print 'le dealer remport la manche'
                print('\n')

            elif condition == 1:
                print 'egalite'
                sam.add_money(mise)

        print('\n')
        print('Vous avez :'), sam.bankroll, 'Euros'
        print('\n')
        print "La partie est fini."
        if sam.bankroll == 0:
            print('\n')
            print "Vous n'avez plus de sous"
            print('\n')
            value = ''
            while value.lower() not in ['yes', 'no', 'y', 'n']:
                value = raw_input("Voulez vous en remettre? [Y/N]")
                print('\n')
            if value.lower()in ['yes', 'y']:
                amount = int(raw_input('combien voulez vous ajouter ?'))
                print('\n')
                sam.add_money(amount)
            else:
                break
        value = ''
        while value.lower() not in ['yes', 'no', 'y', 'n']:
            value = raw_input("Voulez vous refaire une manche? [Y/N]")
        play_game = True if value.lower()in ['yes', 'y'] else False
