# TicTacToe Part A

A two player command line TicTacToe game where player take turns. When prompted to choose the position they wanna play at. Just enter the number based on the counting progression of positions.

## Board and Positions

The initial board looks like

             # # #
             # # #
             # # #

where a hash repersents an empty slot which none of the player has picked yet. As the game progresses the `#` symbols will be replaced by `X` and `O` indicating which player has taken the square.

Positions on the board are counted from the top left, moving right first and then bottom. Let's look at a visual repersentation.

            1 2 3
            4 5 6
            7 8 9

So if you want to in the middle position, you can choose the position 5.

## How to play

`python3 game.py`

_created and tested for python version 3.5_
