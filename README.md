# Boggle Solver/Game

This is a command-line Boggle Solver and Boggle game, written in Python.

To play a game of Boggle, simply run the following command:

```
python boggle.py
```

The utility will display a random 4x4 grid of letters - you have 3 minutes to find as many words in the grid as possible, by moving between adjoining letters vertically, horizontally or diagonally in any direction. Words must be at least 3 letters long, and if the letter 'Q' is shown it should be treated as the 2-letter sequence 'Qu'.

When your time runs out, the utility will show you all the words that it was possible to find in the grid so that you can see how well you did.

To solve a Boggle board (i.e. to find all possible words in the grid), run the following command replacing the argument enclosed in quotes with the letters of the board:

```
python boggle.py "YOUR FOUR ROWS HERE"
```

You must provide exactly 16 letters in groups of 4 as shown above, with each group representing a row of letters from the grid starting with the top row.

