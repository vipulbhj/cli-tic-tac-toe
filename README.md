# TicTacToe Part A

A two player command line TicTacToe game where player take turns. When prompted to choose the position you wanna play at, enter the number based on the game board standard explained below.

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

## How to run tests

Tests are written as `txt` files which will be the input to the program. To run a test simple execute `python3 game.py < test_file_name.txt`.

For example `python3 game.py < tests/player_two_win_invalid_values.txt`
