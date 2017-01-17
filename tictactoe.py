from IPython.display import clear_output
import sys


mem = str()
num = str()
choix = []


def new_board():
    morpion = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    return morpion


def add_player():

        nom = raw_input("Entrez votre nom : ")
        symbol = str()
        symbol2 = str()
        while (symbol.upper() != "X" and symbol.upper() != "O"):
            symbol = raw_input("Quel signe voulez vous ? X ou O ")
        joueur1 = {nom: symbol.upper()}
        mem = symbol.upper()

        nom2 = raw_input("Entrez votre nom : ")
        while (symbol2.upper() != "X" and symbol2.upper() != "O") or (mem == symbol2.upper()):
            symbol2 = raw_input("Quel signe voulez vous ? X ou O ")
        joueur2 = {nom2: symbol2.upper()}
        return joueur1, joueur2


def print_game():
    for i in range(3):
        print ' %s  |  %s  | %s' % (morpion[i*3+1], morpion[i*3+2], morpion[i*3+3])


def check_win():
    if morpion[1] == morpion[2] and morpion[1] == morpion[3]:
        if morpion[1] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[1] == morpion[5] and morpion[1] == morpion[9]:
        if morpion[1] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[1] == morpion[4] and morpion[1] == morpion[7]:
        if morpion[1] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[2] == morpion[4] and morpion[2] == morpion[8]:
        if morpion[2] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[3] == morpion[5] and morpion[3] == morpion[7]:
        if morpion[3] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[3] == morpion[6] and morpion[3] == morpion[9]:
        if morpion[3] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[4] == morpion[5] and morpion[4] == morpion[6]:
        if morpion[4] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    elif morpion[7] == morpion[8] and morpion[7] == morpion[9]:
        if morpion[7] == j1.values():
            print ("Joueur 1 WIN")
        else:
            print ("Joueur 2 WIN")
        sys.exit(0)
    else:
        pass


morpion = new_board()
j1, j2 = add_player()
print_game()

print (" Le jeu va demarer : ")

while (num not in range(1, 10)):
    num = input("Joueur 1 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j1.values()
print_game()
num = 0

while (num not in range(1, 10) or num in choix):
    num = input("Joueur 2 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j2.values()
print_game()
num = 0

while (num not in range(1, 10)or num in choix):
    num = input("Joueur 1 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j1.values()
print_game()
num = 0

while (num not in range(1, 10) or num in choix):
    num = input("Joueur 2 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j2.values()
print_game()
num = 0

while (num not in range(1, 10)or num in choix):
    num = input("Joueur 1 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j1.values()
print_game()
num = 0
check_win()

while (num not in range(1, 10) or num in choix):
    num = input("Joueur 2 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j2.values()
print_game()
num = 0
check_win()

while (num not in range(1, 10)or num in choix):
    num = input("Joueur 1 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j1.values()
print_game()
num = 0
check_win()

while (num not in range(1, 10) or num in choix):
    num = input("Joueur 2 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j2.values()
print_game()
num = 0
check_win()

while (num not in range(1, 10)or num in choix):
    num = input("Joueur 1 choissisez votre case :")
    if(num not in range(1, 10) or num in choix):
        print 'mauvais choix'
choix = choix + [num]
morpion[num] = j1.values()
print_game()
num = 0
check_win()
