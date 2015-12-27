import sys
import time
import signal
import os

from trie import Trie
from board import Board
from cubes import Cubes
from board_search import board_search
from answers import Answers
from progress_bar import ProgressBar
from threading import Event

def play_game(trie):
    letters = Cubes().shuffle()
    board = Board(letters)

    print board
    print 'You have 3 minutes - press Ctrl-C to finish early'

    bar = ProgressBar(60)
    try:
        event = Event()
        for i in range(60):
            bar.show(i)
            event.wait(3)
        bar.finish()
        os.system('say "time is up, stop boggling"')
    except KeyboardInterrupt:
        pass

    raw_input('\nPress <ENTER> to see answers')

    results = board_search(board, trie)
    answers = Answers()
    answers.add(results)

    print answers


def show_answers(trie, letters):
    board = Board(letters)

    results = board_search(board, trie)

    answers = Answers()
    answers.add(results)

    print board
    print answers

if __name__ == '__main__':
    print 'Loading word list, please wait...'
    trie = Trie()
    for w in open('resources/words.txt').readlines():
        word = w.strip()
        if len(word) > 2:
            trie.add(word.upper())

    if len(sys.argv) > 1:
        # Convert the command-line argument into a list of lists of letters
        letters = map(list, sys.argv[1].upper().split(' '))
        show_answers(trie, letters)
    else:
        play_game(trie)



