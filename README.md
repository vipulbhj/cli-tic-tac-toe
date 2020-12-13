# TicTacToe Single Player

A command line TicTacToe game where you player against a computer player and moves are made by taking turns. When prompted to choose the position they wanna play at, enter the number based on the game board standard explained below.

 __A two player version can be found in the [here](https://github.com/vipulbhj/tree/master)__

## Board and Positions

The initial board looks like

             # # #
             # # #
             # # #

where a hash repersents an empty slot which none of the player has picked yet. As the game progresses the `#` symbols will be replaced by `X` (which is YOU) and `O` (which is the computer bot) to indicate the moves made in the game.

Positions on the board are counted from the top left, moving right first and then bottom. Let's look at a visual repersentation.

            1 2 3
            4 5 6
            7 8 9

So if you want to in the middle position, you will choose the position 5.

## How to play

`python3 game.py`

_created and tested for python version 3.5_
