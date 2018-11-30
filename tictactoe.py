#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bertrand Yvernault

INIT_BOARD = {1: None, 2: None, 3: None,
              4: None, 5: None, 6: None,
              7: None, 8: None, 9: None}
WINNING_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                        [1, 4, 7], [2, 5, 8], [3, 6, 9],
                        [1, 5, 9], [3, 5, 7]]


def init_game():
    board = INIT_BOARD
    players = list()
    for ind in range(1, 3):
        print 'Joueur numero %d' % ind
        player = add_player(players)
        players.append(player)
    return players, board


def print_players(players):
    print 'Les joueurs sont :'
    for player in players:
        print ' nom: %s - symbol: %s' % (player['name'], player['symbol'])


def add_player(players):
    good_player_name = False
    while not good_player_name:
        player_name = raw_input("Entrez votre nom : ")
        if player_name not in [p.get('name') for p in players]:
            good_player_name = True
        else:
            print ' Nom deja choisi. Svp tapez un autre nom.'
    good_symbol = False
    while not good_symbol:
        symbol = raw_input("Quel signe choissisez vous ? [X ou O] ")
        if symbol.upper() in ['X', 'O'] and \
           symbol.upper() not in [p.get('symbol') for p in players]:
            good_symbol = True
        else:
            print 'Mauvais symbol.'
    return {'name': player_name, 'symbol': symbol.upper()}


def print_init_board():
    print '-------------------'
    print '|  %s  |  %s  |  %s  |' % (1, 2, 3)
    print '-------------------'
    print '|  %s  |  %s  |  %s  |' % (4, 5, 6)
    print '-------------------'
    print '|  %s  |  %s  |  %s  |' % (7, 8, 9)
    print '-------------------'


def print_board(board):
    print '-------------------'
    for i in range(3):
        val1 = ' ' if not board[i*3+1] else board[i*3+1]
        val2 = ' ' if not board[i*3+2] else board[i*3+2]
        val3 = ' ' if not board[(i+1)*3] else board[(i+1)*3]
        print '|  %s  |  %s  |  %s  |' % (val1, val2, val3)
        print '-------------------'


def check_case(case, board):
    if case not in range(1, 10):
        print "Error: la case n'existe pas. Choissisez entre 1 et 9."
        return False
    elif board[case] is None:  # if the case is not set
        return True
    else:
        print "Error: la case a deja été choissis."
        return False


def play_round(player, board):
    good_case = False
    while not good_case:
        case = raw_input("%s - choissisez votre case: " % player['name'])
        try:
            case = int(case)
            good_case = check_case(case, board)
        except ValueError:
            print "Mauvaise case. Ce n'est pas un entier entre 1 et 9"
            good_case = False
    board[case] = player['symbol']
    print_board(board)
    return board


def check_game(players, board):
    if check_win(players, board):
        return True
    elif None not in board.values():  # Si personne gagne et la jeu est complet
        print 'Le jeu est fini. Pas de gagnant.'
        return True
    else:  # continue de jouer
        return False


def check_row_col_diag(board, comb):
    if board[comb[0]] == board[comb[1]] == board[comb[2]] and \
       board[comb[0]] is not None:
        return True
    else:
        return False


def check_win(players, board):
    for combination in WINNING_COMBINATIONS:
        if check_row_col_diag(board, combination):
            player = [p for p in players if p['symbol'] == board[1]]
            print "%s gagne. Félicitations." % player[0]['name']
            return True
    return False


if __name__ == '__main__':
    value = ''
    while value.lower() not in ['yes', 'no', 'y', 'n']:
        value = raw_input("Voulez vous jouer aux Morpions? [Y/N]")
    play_game = True if value.lower() in ['yes', 'y'] else False
    while play_game:
        players, board = init_game()
        print '\n'
        print_players(players)
        print '\n'
        print_init_board()
        print "\nLa partie de morpions va démarrer."

        game_finished = False
        round_count = 0
        while not game_finished:
            player = players[round_count % 2]
            board = play_round(player, board)
            round_count += 1
            game_finished = check_game(players, board)

        print "La partie est fini.\n"
        value = ''
        while value.lower() not in ['yes', 'no', 'y', 'n']:
            value = raw_input("Voulez vous refaire une partie? [Y/N]")
        play_game = True if value.lower()in ['yes', 'y'] else False
