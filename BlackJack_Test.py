{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "class Player(object):\n",
    "    \n",
    "    def __init__(self, bankroll=1000):\n",
    "        self.bankrool = bankroll\n",
    "        \n",
    "    def add_money(self, amount):\n",
    "        self.bankroll += amount\n",
    "        \n",
    "class Deck(object):\n",
    "    \n",
    "    def __init__(self, paquet):\n",
    "        paquet = []\n",
    "        for suite in ['coeur', 'pique', 'carreau', 'trefle']:\n",
    "            for carte in range (1,15):\n",
    "                carte_nb = carte\n",
    "                if carte_nb == 11:\n",
    "                    carte_nb = 'V'\n",
    "                elif carte_nb == 12:\n",
    "                    carte_nb ='D'\n",
    "                elif carte_nb == 13:\n",
    "                    carte_nb ='R'\n",
    "                elif carte_nb == 14:\n",
    "                    carte_nb ='A'\n",
    "                paquet.append({'suite': suite, 'carte': carte_nb})\n",
    "        self.jeu = paquet\n",
    "    \n",
    "\n",
    "sam = Player()\n",
    "deck = Deck(jeu)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'carte': 1, 'suite': 'coeur'}"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
